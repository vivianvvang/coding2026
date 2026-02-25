# 1. Input Data
expenses = [
    {"expense_id": "001", "trip_id": "001", "amount_usd": "49.99", "expense_type": "supplies", "vendor_type": "restaurant", "vendor_name": "Outback Roadhouse"},
    {"expense_id": "002", "trip_id": "001", "amount_usd": "125.00", "expense_type": "supplies", "vendor_type": "retailer", "vendor_name": "Staples"},
    {"expense_id": "003", "trip_id": "002", "amount_usd": "153.00", "expense_type": "meals", "vendor_type": "restaurant", "vendor_name": "Olive Yurt"},
    {"expense_id": "004", "trip_id": "002", "amount_usd": "1996.00", "expense_type": "airfare", "vendor_type": "transportation", "vendor_name": "Southeast Airlines"},
    {"expense_id": "005", "trip_id": "002", "amount_usd": "34.68", "expense_type": "meals", "vendor_type": "restaurant", "vendor_name": "The Great Grill"},
    {"expense_id": "006", "trip_id": "002", "amount_usd": "22.40", "expense_type": "meals", "vendor_type": "restaurant", "vendor_name": "The Great Grill"},
    {"expense_id": "007", "trip_id": "003", "amount_usd": "59.50", "expense_type": "entertainment", "vendor_type": "theater", "vendor_name": "Silver Screen"}
]

# 2. Core Classes (Data Models)
class Rule:
    """Stores the logic for a single rule as pure data."""
    def __init__(self, name, target_field, operator, threshold, 
                 match_field=None, match_value=None, group_by=None, scope="individual"):
        self.name = name
        self.scope = scope                # 'individual' or 'group'
        self.target_field = target_field  # field to check (e.g., 'amount_usd')
        self.operator = operator          # 'max' or 'forbidden'
        self.threshold = threshold        # limit or forbidden string
        
        # Optional filters
        self.match_field = match_field    # e.g., 'vendor_type'
        self.match_value = match_value    # e.g., 'restaurant'
        
        # Required for group rules
        self.group_by = group_by          # e.g., 'trip_id'

class Violation:
    """Stores the result of a broken rule."""
    def __init__(self, expense_id, rule_name, actual_value):
        self.expense_id = expense_id
        self.rule_name = rule_name
        self.actual_value = actual_value

    def __repr__(self):
        return f"Flagged [{self.expense_id}] | Rule: '{self.rule_name}' | Value Found: {self.actual_value}"


# 3. The Engine Class (Stateless Logic)
class ExpenseEvaluator:
    """Evaluates a list of rules against a list of expenses."""
    def __init__(self, rules):
        self.rules = rules

    def _get_float(self, value):
        """Safely converts amount strings to floats."""
        try:
            return float(value)
        except (TypeError, ValueError):
            return 0.0

    def evaluate(self, expenses):
        violations = []
        for rule in self.rules:
            if rule.scope == "individual":
                violations.extend(self._evaluate_individual(rule, expenses))
            elif rule.scope == "group":
                violations.extend(self._evaluate_group(rule, expenses))
        return violations

    def _evaluate_individual(self, rule, expenses):
        results = []
        for exp in expenses:
            # Check if this rule applies to this expense based on match conditions
            if rule.match_field:
                if exp.get(rule.match_field) != rule.match_value:
                    continue  # Skip if it doesn't match the filter

            value = exp.get(rule.target_field)
            
            # Cast to float if we are doing math
            if rule.target_field == "amount_usd":
                value = self._get_float(value)

            # Apply operator logic
            if rule.operator == "max" and value > rule.threshold:
                results.append(Violation(exp["expense_id"], rule.name, value))
            elif rule.operator == "forbidden" and value == rule.threshold:
                results.append(Violation(exp["expense_id"], rule.name, value))
                
        return results

    def _evaluate_group(self, rule, expenses):
        results = []
        groups = {} # Dictionary to hold sums

        # Step 1: Group and Sum
        for exp in expenses:
            group_id = exp.get(rule.group_by)
            
            # Filter rows before summing (e.g., only sum "meals")
            if rule.match_field:
                if exp.get(rule.match_field) != rule.match_value:
                    continue
            
            amount = self._get_float(exp.get(rule.target_field))
            groups[group_id] = groups.get(group_id, 0.0) + amount

        # Step 2: Check limits against the summed groups
        for group_id, total in groups.items():
            if rule.operator == "max" and total > rule.threshold:
                results.append(Violation(group_id, rule.name, round(total, 2)))
                
        return results


# 4. Configuration (Treating Policy as Data)
system_rules = [
    # Part 1: Individual Rules
    Rule("Restaurant > $75", "individual", "amount_usd", "max", 75.0, match_field="vendor_type", match_value="restaurant"),
    Rule("No Airfare", "individual", "expense_type", "forbidden", "airfare"),
    Rule("No Entertainment", "individual", "expense_type", "forbidden", "entertainment"),
    Rule("Max Single Expense $250", "individual", "amount_usd", "max", 250.0),
    
    # Part 2: Group Rules
    Rule("Trip Total > $2000", "group", "amount_usd", "max", 2000.0, group_by="trip_id"),
    Rule("Trip Meals > $200", "group", "amount_usd", "max", 200.0, group_by="trip_id", match_field="expense_type", match_value="meals")
]

# 5. Execution
engine = ExpenseEvaluator(system_rules)
found_violations = engine.evaluate(expenses)

print("--- Evaluation Results ---")
for v in found_violations:
    print(v)