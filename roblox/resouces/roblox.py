1. flatten nested array
分别用递归和非递归写

# https://www.1point3acres.com/bbs/thread-1134637-1-1.html

2. 一共面了2轮代码，一轮系统设计

1.coding1: 一个亚裔小哥，问给一个log数组，给一个n代表每一页log capacity，给一个i代表page的index，让返回一个数组，数组里每一个数代表这个cursor开头的log id。
写完以后发现还有第二题，现在给多个log数组，同样给每一页可以放多少log的n和page index，让你反回同样的结果。但是是所有log数组的合并结果。这个题有点类似于离叩珥霰。
2.coding2：国人小哥，问的是地里那道给你一个list of call functions问最高频的stack trace是哪一个，小哥人很好
3.sd 问部署一个roblox的release的workflow的设计，偏cicd这方面的

# https://www.1point3acres.com/bbs/thread-1134043-1-1.html


3. 地里经典，是给一些log让你实时返回这个event是不是有效的。要求是每个用户只能在一段时间内发出定量的event。有点类似于叁柳饵。
# https://www.1point3acres.com/bbs/thread-1133689-1-1.html


4. 然后约tech screen，问的是给日志，怎么判断
哪个function被call的最多，如果一样多的return第一个。日志的格式是有开始结束marker，像
> main
> a
> b
< b
> b
< b
< a
> a
< a
< main
没有recursive call。要过test case
# https://www.1point3acres.com/bbs/thread-1133301-1-1.html


5. 一道关于rate limiter的题目

给你请求数组(timestamps) 最多窗内请求数 窗户大小
返回是否允许请求 e.g. [true, true, false, true]
题目不难 但是没有把队列清除过期时间戳的条件想清楚 最后结果不对
面试官提示了很多 之后要多练习啊
# https://www.1point3acres.com/bbs/thread-1132889-1-1.html


6. 三轮
coding，把寺旧。不过要print座位。写了解法，一开始有bug，改了会。
hm, 正常聊天问简历，少量bq。
sd, 类似reward payment。

# https://www.1point3acres.com/bbs/thread-1131207-1-1.html

7. 一道dfs，player根据当前cell值（J, W）可以跳格子或走格子，问能不能到终点。
follow-up是最短路径。
# https://www.1point3acres.com/bbs/thread-1131203-1-1.html


8. [SD] 设计一个共享的待办事项。
体验不是很好，大概面试官有自己想要考察的点，我在说的时候不停地被打断。
# https://www.1point3acres.com/bbs/thread-1131094-1-1.html


9. [SD] 店面内容是射击，一个待办列表爱普，需支持共享、实时办公、列表更新通知协同用户等功能。
是常见题，楼主是有准备的，无奈面试经验不足。面试官是一位印哥，算和善，聊很嗨，还主动推销他们组。然而可能乖楼主面试经验不足，
讲的顺序被面试官牵着鼻子走，遂只画了整体流程图，讲了API，口述了Flow，深挖了如何存储、通知、在线共享、信息队列等话题。
可能就是前面要求确认太久，后面得到的反馈是回答不够完整比如没有讲到schema。
# https://www.1point3acres.com/bbs/thread-1130292-1-1.html

10. 好像没在店里看到这题, 
input如下, ->代表function call, <- 代表function return, 
output是frequency最高的call stack,
这个例子里就是"main->eventClick->eventClickAction". frequency是2， 1, 2, 3行是第一次出现, 1, 2, 5行是第二次出现 （3, 4行可以看作是offset了，我的理解）求加米！！！
traces=[
"-> main",
"-> eventClick",

"-> eventClickAction",
"<- eventClickAction",
"-> eventClickAction",
"<- eventClickAction",
"<- eventClick",
"<- main",
]
#  https://www.1point3acres.com/bbs/thread-1130087-1-1.html


11. 面试官：一个principle，一个senior shadow。

面试问题：有个game dashboard。里面显示一些游戏。每个游戏都需要显示 哪些朋友玩过，并且显示 like 数量。
# https://www.1point3acres.com/bbs/thread-1129830-1-1.html


12. [SD] code轮是prefix题，具体的在另外一个回复了。

system design第一场是实现支持delayed payment的payment system.  比较关注delay payment的实现，各个部分出错怎么处理。 有个 follow up怎么保证payment的正确时序性，如果两个payment之间有相互依赖，前一个因为出错了要retry, 可能会在后一个request的后面处理，这种情况怎么办。
当时我的回答的是可以给有强依赖的request events （比如来自同一个用户相关的payment请求)放到一个子queue里顺序执行，只有第一个执行完了再处理下一个.  但这个实现可能会比较复杂。 另外一个想法就是如果因为时序依赖照成某些payment失败，直接返回给用户，让用户自己根据实际情况是否重试， 后一个实现简单可行。这个是我但是能想到的两个选项，给面试官分析了下，他还比较满意。
第二场system design是经常出现的To do list,  这个就是按部就班讲function/non function requires,  API design, DB design 和high level arch,   Deep dive了更新task / task list的流程，本来还要讲怎么用Operational Transformation来是实现多人同享edit. 但Interviewer 因为快没时间了也没有想探讨细节。

BQ轮最重要的是要讲一个most proud project, 讲下probelm/goal,  your role & contribution, challenges & solution,  impact & output,  Retro/Learnings.

# https://www.1point3acres.com/bbs/thread-1128836-1-1.html


13. 蛮solid的面试
五轮，四轮利口 + 模型设计讨论/project deep dive，一轮HM BQ

四轮利口分别是 奇异伞，五六零变形，物流+一道bucket sort忘记题目，七九 follow up 二一二
# https://www.1point3acres.com/bbs/thread-1128681-1-1.html


14. 剩20min考一道经典老题 利口 贰佰
# https://www.1point3acres.com/bbs/thread-1128679-1-1.html


15. 然后一道地里利口老题·一把伞丝
# https://www.1point3acres.com/bbs/thread-1128678-1-1.html


16. [SD] 新鲜出炉的SD

跟题库大差不差，like/unlike，1M的traffic read 100k的write
show leaderboard， see your fav list.
问了问怎么处理1M的 qps， 用了kafka， batch job，snapshot
还不知道结果，最近组里毒的不行，想离开了，先发出来求好运

# https://www.1point3acres.com/bbs/thread-1128104-1-1.html


17. [SD] 讲一下我遇到的两道系统设计
Consent piping. 设计一个系统能够read以及pipe用户privacy相关的consent。我答得不是很好
To do list. 设计一个待办事项系统，用户可以在里面新建，分享，多人编辑一个list。这个我就是按照google doc答的

# https://www.1point3acres.com/bbs/thread-1124869-1-1.html


18. remove string that is prefix of other string in an array. The ordering needs to be the same as the input
# https://www.1point3acres.com/bbs/thread-1123993-1-1.html


19. 1- 45分钟 题库里面的 Coding: experience Scheduler
利口原题 621
其实之前写过，但是写的时候还是还是有点紧张，写了一个heap解法，忘记了有linear 解法，虽然linear的口里描述出来，但是没有implement完

# https://www.1point3acres.com/bbs/thread-1123499-1-1.html


20. 第一问
写一道判断func是不是输入完成的函数叫isFuncComplete，比如
print( -> false
print() -> true
输入一个string，返回bool，不需要判断太复杂的逻辑，面试官其实只需要判断括号是不是对齐了


第二问
括号种类升级到了（【{，需要进行上面的类似判断


第三问
额外增加了引号，判断是否输入完成
# https://www.1point3acres.com/bbs/thread-1123048-1-1.html

21. An offline music player has a playlist of songs and the following two modes：
Random – at each step, picks the next song uniformly at random from the entire playlist (with “replacement,” so the same song can appear back-to-back).
Shuffle – often interpreted iPod‐style:
The player randomly permutes the entire playlist (each song appears exactly once in that permutation).
It then plays through that permutation in order.
Once all songs have been played, it (optionally) picks a new random permutation and starts again.

You start listening in the middle of whatever the player is doing. You hear a short sequence of songs, then you stop. 问题：“Could the sequence I heard come from ‘shuffle’ mode?”
然后给了一些example:
["A", "A", "A"]
复制代码
→ labeled # shuffle
["A", "B", "C"]
复制代码
→ labeled # random
["A", "A", "C", "A"]
复制代码
→ ???
["A", "C", "A", "B", "A", "C", "B", "G"]
复制代码
→ ???
#  https://www.1point3acres.com/bbs/thread-1122435-1-1.html


22. input:
list of int : [1,2,3,4,5,6,7,4,23,1]

int: amount of segment
output: random 的 output input list 里的 int 到 segment里
example
input: [1,2,3,4,5,6] segment number 2
output: [[2,5,6], [1,3,4]]

# https://www.1point3acres.com/bbs/thread-1122032-1-1.html


23. [SD] 刚面了 Roblox 系统面试
题目是板上时常看到的 payment system

重点是如何实现延迟支付
还有一个重点就是在peak traffic的时候 你design的系统哪里会出现 bottle neck
# https://www.1point3acres.com/bbs/thread-1122024-1-1.html


24. [SD] 叫设计一个支付系统，支持游戏里的货币从一个账户转账给另外一个账户，然后需要支持两种query：

第一是对每一个账户需要知道过去24小时内的总收支
第二是对每一个账户需要返回过去30天内每小时的余额，大概就是一个时间序列
感觉就是设计一个钱包然后在做点统计

# https://www.1point3acres.com/bbs/thread-1121249-1-1.html


25. [SD]: like/unlike 面经高频
有三个要求：
用户可以like/unlike any item
用户可以看到任意item like count
用户可以看到所有自己liked items
# https://www.1point3acres.com/bbs/thread-1119942-1-1.html


26. 第二轮是coding店面。

ID manager管理[1, MaxLong]的id。实现两个api：
acquire(): 返回pool中最小的id。
release(id):把id返回到pool。
# https://www.1point3acres.com/bbs/thread-1118352-1-1.html


27. 柳兒依
# https://www.1point3acres.com/bbs/thread-1114884-1-1.html


28. [SD] 电面 就是地里常见的给list of strings 删除其他string的prefix的string。 follow up：删除其他string的substring
SD：设计instagram，重点是 post下面实现： “Tom, James”（用户关注的人）and 500k people liked this post.
# https://www.1point3acres.com/bbs/thread-1114194-1-1.html


29.[SD] onsite 总共3 轮，没有coding。
system design。 设计一个payment service，并且可以支持延迟支付，可以assume 已经有类似stripe 之类的service 
处理actual 的transaction，还要支持怎么cancel 一个scheduled 的payment。qps 要求5k，如何避免重复操作。
面试的时候先从api入手，定义interface。
第二个sd 完全根据本人简历，面试官随机出的一个design。
# https://www.1point3acres.com/bbs/thread-1113035-1-1.html


30. 面试小哥是个国人，题目是地里的那个log timestamp的高频题，follow up我是用的map 存每个timestamp 的entry，val 就是一个list，
因为需要记录所有信息。follow up 之后，又发散性的问了在分布式的情况下怎么处理。
# https://www.1point3acres.com/bbs/thread-1113033-1-1.html


31. 24年冬电面，内推的，target IC3/4，面试官国人，上来一道自创Trie hard，写完后过了初始test case，后续又加了几个test case，有一种没过，
一直debug不出来，挂。麻了


["a","abc","abc hello","bc"]
string array，如果里面有string是另一个string prefix，remove prefix, and keep remaining string order same
answer: ["abc hello","bc"]
# https://www.1point3acres.com/bbs/thread-1112306-1-1.html


32.[SD] Phone (面經題)
從log裡檢查ip是否為bot. 會給你input string, 每一行是timestamp及ip. 從給定的threshold輸出哪些ip是bot就行.
follow-up是給你list of timestamp及ip, 每次輸入timestamp及ip時判斷這個ip是否為bot.


VO

coding:
沒見過的題, 這輪完全不懂面試官想問什麼.. 甚至覺得他自己也沒100%了解題目, clarify了半天有時他也不知道這output是不是valid的. 
但大致上就讓你random generate一個數然後開始填matrix, 其中任一行任一列都不能是全部一樣的數. 
感覺這part是為了下一個part的輸入做準備, 沒能進到follow-up時間就到了.


SD:
todo list, 能share, 能和別人一起update同一個list.
這輪感覺說的不夠deep dive.


HM:
常規bq, projects deep dive.
知道coding準掛後就把這輪當練習了沒特別再準備, 當聊天.

# https://www.1point3acres.com/bbs/thread-1111858-1-1.html


33. 第一题栗口巴丝旧， 时间比较紧没有写完。

第二题不是栗口也没题干，就是给一个method要求写验证用户输入。最开始有点蒙圈，反复确认了很久要求是什么，最后写出来跑了test。
# https://www.1point3acres.com/bbs/thread-1106283-1-1.html


34. [SD]
SD1: 常考的TODO list，地里有, 就是能创建，修改to do list，然后特别的是能和朋友share，朋友也能update，我也问了是不是纯text，
面试官说提前问到了他follow up的问题，就是希望可以扩展成支持多media...其实和盆友share也是面试官之后准备的，但是都被我提前问出来了，多问吧...


SD2: 因为我面的组是做data security/IAM的，所以这轮面了个设计authorization service，也就是各个组用这个service来确定什么人能有什么权限，
提供allow or deny decision，必然的就是这个decision必须要非常快，我之前工作其实做过类似的，面试官也做过类似的，
巧的是他之前和我是一个公司的，只是他待了11年，曾经一度拥有同一个skip manager，我说的技术点他都知道，毕竟他从毕业就在，职业技术语言都是从那来的
# https://www.1point3acres.com/bbs/thread-1103965-1-1.html


35. 面的是data privacy/security组的后端




Remove prefix strings in a list of string.
比如 {"a", "ab", "abc"}， output: {"abc"}.
{"a", "bc", "ab", "abc hello"} ， output: {"bc", "abc hello"}.
要求output array 要保持string 在input 里的顺序


# https://www.1point3acres.com/bbs/thread-1103963-1-1.html


36. interview summary
# https://www.1point3acres.com/bbs/thread-1102710-1-1.html

[SD]
Like/unlike
SD: 提供点赞功能，能看到自己的点赞，也能看到每个东西总共被几个人点过赞
    这轮应该是挂了。因为我犯了严重错误，冲进去太急了，design上来先丢了查看一个东西自己是否点赞过这个功能，然后查看商品总点赞时忽略了那个是看count，而且没有clarify这个精准度。精准度这个是后来面试官challenge，还提到youtube的点赞数其实经常是estimated number比如1.5M而不是15xxxxxx这么精准的。
    虽然最后还是成功做完了全部的flow，也deep dive了两个点。但是之前的那两个大red flags，能过个鬼。
# https://www.1point3acres.com/bbs/thread-1096710-1-1.html


Top k popular games
店面就是SD，要求设计一个rating system，展示Top 50 popular games。 Popularity就是每个game的在线人数。考点是排序和concurrency。
# https://www.1point3acres.com/bbs/thread-1077946-1-1.html


设计ins
面试官一开始是要求不需要考虑scale，用现有的工具，最快时间设计一个可以work的版本。中间有问一些问题，有些忘了，现在记得的有：有考察一下user registration怎么简单处理（这里我不太会），
db应该用什么，client端怎么选技术栈等等。
# https://www.1point3acres.com/bbs/thread-1083175-1-1.html

Team account
有两种账户： personal account, team account
设计一个转账系统，同一个team里的成员可以给从personal account给team account转钱。

要求实现
1. 转钱
2. 过去24小时/30天team account balance变化
# https://www.1point3acres.com/bbs/thread-1078111-1-1.html


In-memory Gaming platform
等到面试那天，面试官要求设计一个in memory 的gaming platform。当时真的傻眼了，事关我好久没玩游戏了，连他要我做什么都不知道。
而且in memory的话，那就是等于low level的设计，要写code实现…

大概的意思是，玩游戏的人有各种level的，你怎样设计一个游戏平台让他们排队玩游戏。队伍等到100人之后就会开启游戏。规定每个人每次只能排一个队。
# https://www.1point3acres.com/bbs/thread-1099669-1-1.html


延迟放款系统
设计一个系统handle延迟放款给用户



37. 
是没见过的新题，我真的是新题体质，从没遇到过面经。如果有人见过这道请告知。
让实现一个ID pool，ID的range是1到max long。有俩API acquire（）和release（），前者返回一个最小的空闲的id，后者收回一个正在使用的ID，把它重新放回池子。
我用了一个min heap来存available的IDs，一开始先只把1放进去。只有当heap空了的时候，放入下一个available的ID。在release的时候再把ID放回heap。
再用一个set来存放正在使用的ID。大家有更优解，请不吝赐教。
这道题，我分析可能挂在复杂度分析，我说这两个function的时间都是O(logn)，n是max long，但具体说acquire的时候我记成heap poll（）的复杂度是O（1）了，应该是O（logn）的。估计挂这里了。但我代码能跑，用各种edge cases也测过了。
但是感觉面试官follow我的思路有点疑惑，也许这不是她期待的解法。欢迎大家讨论。
# https://www.1point3acres.com/bbs/thread-1102457-1-1.html


38. Tech Interview: basic hashmap question with follow up


以下内容需要积分高于 140 您已经可以浏览

# You're running a pool of servers where the servers are numbered sequentially starting from 1.


# Over time, any given server might explode, in which case its server number is made available for reuse. 
# When a new server is launched, it should be given the lowest available number.  


# Write a function which, given the list of currently allocated server numbers, returns the number of the next server to allocate. 
# In addition, you should demonstrate your approach to testing that your function is correct.


# You may choose to use an existing testing library for your language if you choose, or you may write your own process if you prefer.  


# For example, your function should behave something like the following:  
#   >> next_server_number([5, 3, 1])
#   2
#   >> next_server_number([5, 4, 1, 2])
#   3
#   >> next_server_number([3, 2, 1])
#   4
#   >> next_server_number([2, 3])
#   1
#   >> next_server_number([]) #   1
#   >> next_server_number([1,1.5,2,2.5,3,3.5,4,5,5.5])
#   6
#   >> next_server_number([2.5])

# https://www.1point3acres.com/bbs/thread-1098941-1-1.html


39. [SD] 楼主第一次面sd，挂了。题目就是面筋里见过的Design like/unlike system，没想到就这么华丽丽地遇到了。要实现的功能有，
1. 用户可以like/unlike a item 2. 用户可以看自己like的items 3. 用户可以看item的like count。每个功能都直接给了QPS，不用自己算了，但楼主忘了具体数了，就按最大来设计吧。
# https://www.1point3acres.com/bbs/thread-1097142-1-1.html


40.  [SD]
它家coding题都很面经的，老老实实刷地里就能全cover。


店面: 🔗 www.1point3acres.com


VO: 过了店面以后VO就没coding了。
SD: 提供点赞功能，能看到自己的点赞，也能看到每个东西总共被几个人点过赞
    这轮应该是挂了。因为我犯了严重错误，冲进去太急了，design上来先丢了查看一个东西自己是否点赞过这个功能，然后查看商品总点赞时忽略了那个是看count，而且没有clarify这个精准度。精准度这个是后来面试官challenge，还提到youtube的点赞数其实经常是estimated number比如1.5M而不是15xxxxxx这么精准的。
    虽然最后还是成功做完了全部的flow，也deep dive了两个点。但是之前的那两个大red flags，能过个鬼。
Project Deep Dive: 做的一般。按SD思路画了说了的。但是自我复盘，被提问的点回答的并没有给足signal显示自己的各项能力。
BQ: 常规题。


挂的心服口服。积累经验了，继续努力。


# https://www.1point3acres.com/bbs/thread-1096710-1-1.html


42. 面试官挺好的一个小姐姐，题目也正常，但是时间到了，吃不准她想看到的优化是什么。
在online ide 里面跑，会提供 input，需要run

同一题的两问：
part 1. 给 时间 和 IP， 看在提供的input里面如果ip 超出了一个threshold，判断为机器人，output 机器人的ip

input: following string, and threshold


1, ip1
1, ip2
1, ip1
4, ip1
4, ip2
5, ip3

isBot(String input, 3) -> ip1
isBot(String input, 2) -> ip1, ip2

isBot(String input, 1) -> ip1, ip2, ip3

part 2. 给 时间 和 IP, 但是有需要看 sliding time window 里面的 ip 数量 超出了一个 threshold，output true/false

# class CheckBot {
#     public CheckBot(int threshold, int windowSize) {

#     }


#     public boolean isBot(int timestamp, String ip) {

#     }

# }

# example:
# Checkbot cb = new CheckBot(threshold = 3, sliding time size = 3);

# isBot(0, ip1) -> false

# isBot(1, ip1) -> false
# isBot(1, ip1) -> true // reached threshold 3 within the time window of 3
# isBot(4, ip2) -> false
# isBot(5, ip1) -> false

# https://www.1point3acres.com/bbs/thread-1086843-1-1.html

43. 发个面经攒人品。下午面的。国人小哥。

Remove prefix strings in a list of string.


Example 1: input  {"a", "ab", "abc"} -> output: {"abc"}.
Example 2: input {"a", "bc", "ab", "abc hello"} --> output: {"bc", "abc hello"}.

要求： output array 要保持String 在input 里的顺序。比如第二个例子: {"abc hello", "bc"} 顺序就不对了。。。

写了最简单的遍历方法。分了一下时间复杂度。提了一下 trie 的解法。没时间写。不管结果怎么样。小哥人挺nice。全程帮忙改typo. experience 不错。
# https://www.1point3acres.com/bbs/thread-1096467-1-1.html


44. 读一个 csv 文件，文件里有10k+ rows，每一行有三个element，game id， game score， quality （good/bad）


有个threshold（比如 65%），题目要求选一个score，所有大于这个score 的 game 里面 bad game 比例不低于 threshold

output 最小的game score，game score 不一定是input 里面的score。比如，game 1， 20， good； game 2， 30， good； game3， 40， bad ； game4，40， bad； game5 50 bad。 答案是21，因为大于21 的score 有4个游戏，三个是bad，一个是good，所以[21, 30] 都满足theshold 要求，选择最小的。
# https://www.1point3acres.com/bbs/thread-1092327-1-1.html



45. 面试官是白人小哥，人挺好的，题目是地里出现过的generate email的题，情景是给三个input，然后output是email body string

第一个input是一个list of detected key words，比如 “hack”，比如“heroin”
第二个input我记不清了，好像是list of string，每个string是keyword to category的mapping，e.g.：["heroin,Drug"]

第三个input是一个list of strings，每一个string是category到instrction的mapping，e.g.：["drug,    Please be aware of drug dealing in the game, report to police if necessary"]
然后输出的email body就是告诉用户，游戏里有XXX类型的关键词被检测到了，你可以按照XXX instructions做。

题不难，主要就是一点字符串处理(大小写，split，join之类的)，我还google了怎么删除strings里的leading spaces，感觉并不影响通过。

这题做完之后还有一个followup，是问如果下游组近期收到的email是之前的三倍，看你会怎么investigate，你可以提问题，面试官会回答，最后找到原因。不知道这个占面试考察多大比例。

# https://www.1point3acres.com/bbs/thread-1091842-1-1.html

店面
之前地里出现过但感觉不是高频：
input如下, ->代表function call, <- 代表function return, output是frequency最高的call stack,
这个例子里就是“main->eventClick->eventClickAction". frequency是2， 1, 2, 3行出现一次, 1, 2, 5行是第二次出现。用栈做的。followup是除了输出call stack还输出次数
traces=[
"-> main",
"-> eventClick",
"-> eventClickAction",

"<- eventClickAction",
"-> eventClickAction",
"<- eventClickAction",
"<- eventClick",
"<- main",
]


VO：
SD。之前出现过：“Game matching system

- 1M DAU, 很多games。user选择加入游戏后，进入到waiting room，系统根据user skill来安排相近level的users组局，组局成功后直接开始游戏；user skill可以通过一个API获得，0-100。需要自己给出一些限制，比如user等待时间不能太久，组局的人数设定有可能是动态的（玩家很少的时候有可能把游戏开始的最少人数变少。之前帖子里还提到过的：设计游戏匹配系统，有很多很多游戏要匹配. 要考虑系统能scale到匹配千百个游戏，像能够处理burst of data的这种消息队列要加上。要考虑region，server clusters是在不同region的。还要讨论server怎么跟client连接，这个回路也要讨论”


2. SD。delayed payment system。引用之前帖子：“重点是如何实现延迟支付。还有一个重点就是在peak traffic的时候 你design的系统哪里会出现 bottle neck discuss solution，还要支持怎么cancel 一个scheduled 的payment。qps 上k，如何避免重复操作
3. 讲一个自己做过的complex system

最后Executive round是纯behavior但问的不简单，都是比较尖锐的需要反映你的weakness的问题

Coding:
given a integer list, a target index and a window size n, return all sublist with size n that contain target index (easy).
Followup: among all sublists from last question, find the one that contain most # of target number, (if equal, return the smaller index one). 这题用prefix sum+sliding window做。

 
"""
=========================CODING/DESIGN SUMMARY===============================
https://www.1point3acres.com/bbs/thread-1027485-1-1.html
"""

"""
SD。之前出现过：“Game matching system

- 1M DAU, 很多games。user选择加入游戏后，进入到waiting room，系统根据user skill来安排相近level的users组局，
组局成功后直接开始游戏；user skill可以通过一个API获得，0-100。需要自己给出一些限制，比如user等待时间不能太久，组局的人数设定有可能是动态的（
玩家很少的时候有可能把游戏开始的最少人数变少。之前帖子里还提到过的：
设计游戏匹配系统，有很多很多游戏要匹配. 要考虑系统能scale到匹配千百个游戏，像能够处理burst of data的这种消息队列要加上。
要考虑region，server clusters是在不同region的。还要讨论server怎么跟client连接，这个回路也要讨论”

7. Consent piping. 设计一个系统能够read以及pipe用户privacy相关的consent。我答得不是很好


"""


46. [sd]: 面经汇总
1. personal account, team account设计一个转账系统，同一个team里的成员可以给从personal account给team account转钱。
要求实现 1. 转钱 2. 过去24小时/30天team account balance变化感觉面试官‍‍‌‍‌‌‍‍‌‍‌‍‌‍‌‍‍‌‌更关注API design， 而不是scalability这些

叫设计一个支付系统，支持游戏里的货币从一个账户转账给另外一个账户，然后需要支持两种query：

第一是对每一个账户需要知道过去24小时内的总收支
第二是对每一个账户需要返回过去30天内每小时的余额，大概就是一个时间序列
感觉就是设计一个钱包然后在做点统计


2.要求设计一个rating system，展示Top 50 popular games。 Popularity就是每个game的在线人数。考点是排序和concurren‍‍‌‍‌‌‍‍‌‍‌‍‌‍‌‍‍‌‌cy。


3. 多人协作的绘图板. Web app要求能拖拽Note，写Note，freeform笔迹，画visio里的各种方块图，能看到别人鼠标的位置，实时互动。
因为面试官直接演示了界面，所以UI设计直接省去了，然后讲了讲需要用到的service API，视图的数据结构怎么样的，如何同server进行sync，如何实时同步，
如何推送实时ev‍‍‌‍‌‌‍‍‌‍‌‍‌‍‌‍‍‌‌ents，如何做full sync，今后如何扩展新的涂鸦类型。


4. 设计todo list，重点在跟朋友分享 有点像google doc，但不用那么复杂
system design是经常出现的To do list,  这个就是按部就班讲function/non function requires,  API design, DB design 和high level arch,   
Deep dive了更新task / task list的流程，本来还要讲怎么用Operational Transformation来是实现多人同享edit. 但Interviewer 因为快没时间了也没有想探讨细节。
To do list. 设计一个待办事项系统，用户可以在里面新建，分享，多人编辑一个list。这个我就是按照google doc答的
todo list, 能share, 能和別人一起update同一個list.

- 要求能handle concurrent editing
- 允许users相互share，共同编辑
- The application should allow a single user or team of users to keep track of a list of tasks to do in the
future. Example:
- 1. John creates a list named "Grocery shopping list"
- 2. John adds task Buy Tomatoes to Grocery Shopping List
- 3. John adds task Buy Onions to Grocery Shopping List
- 4. John completes task Buy Onions from Grocery Shopping List
- 5. John has 1 TODO list with 2 tasks B
- 设计一个checklist application，可以允许多人share并协同工作，需要支持：添加list，添加
item，删除item，标记完成，分享list。考察的比较细致，data model, api design, protocol，
scalability都有考察到，甚至还写了点sql


其次是不同人有不同的role，从基础的viewer（可以增加或者完成
task），到editor（可以改task名字什么的），到admin（可以创建删除todo list之类的）。讨论
内容有API， data model， database选择，如何把某个client的改动及时同步到别的clients里
面，
一个todo list里面collaborator太多读写流量太大怎么办之类的。


5. 罗波罗斯有很多游戏，每个游戏会运行在不同的机器上, 每一台机器会定期的汇报该机器的状态（目前有多少玩家，CPU和内存使用状况）


6. like/unlike，1M的traffic read 100k的write
show leaderboard， see your fav list.
问了问怎么处理1M的 qps， 用了kafka， batch job，snapshot

Like/unlike
SD: 提供点赞功能，能看到自己的点赞，也能看到每个东西总共被几个人点过赞
    这轮应该是挂了。因为我犯了严重错误，冲进去太急了，design上来先丢了查看一个东西自己是否点赞过这个功能，然后查看商品总点赞时忽略了那个是看count，
而且没有clarify这个精准度。精准度这个是后来面试官challenge，还提到youtube的点赞数其实经常是estimated number比如1.5M而不是15xxxxxx这么精准的。
    虽然最后还是成功做完了全部的flow，也deep dive了两个点。但是之前的那两个大red flags，能过个鬼。
1. 用户可以like/unlike a item 
2. 用户可以看自己like的items 
3. 用户可以看item的like count。每个功能都直接给了QPS，不用自己算了，但楼主忘了具体数了，就按最大来设计吧。

- User favorite/unfavorite games
- 需要支持几种queries，包括user->favorite games, (user, item)->favorited?，以及item-># of
favorites
- 可以支持user label他喜欢的item， 然后需要能支持给一个user返回他喜欢的item；给一个
item，‍ ‌‌‍‌‌‌‍‌‍‌‌‍‍‍‍‍‍ 返回总共多少人喜欢
- The user’s click should be shown to the user ASAP, and the user table should always be true of t‍‍‍‍‌‌‍‌‌‌‍‌‍‌‌‍‍‍‍‍‍ he
source.
- 都是like/dislike相似的题，按着topK和ads count的思路设计的。其实就是大量数据的实时处
理，和low latency延迟显示

- 经典count like题目，
一些follow up 类似客户端缓存，write-ahead-log 和 aggregator来减少QPS
- 你就去看下alex xu新书的那个ads click设计 差不多的
- like/dislike counts: Design like count for Roblox Platform Item. 实现1. 一个user可以看到自己所
有的like的item，1M QPS。2. 一个user可以like/unlike item，100k QPS。3‍‌‌‌‌‌‍‌‍‌‍‌‍‍‍‌‌‍‌‍‌ . 可以看到每个item
的like count，1M QPS。主要focus在怎么保证high qps，like count可以eventual consistency, 实
现一个和二需要怎么保证read after write consistent。还有各种数据库的设计，哪里需要放
cache等等



设计instagram，重点是 post下面实现： “Tom, James”（用户关注的人）and 500k people liked this post.
Design Instagram
- 设计个api gateway
- design user tracking event system. 10B event per day. 1k event type. support api get(start, end, topK)
返回时间断内topK event type count. need to design event type, handle gdpr, data
replication,partition etc.


7. Consent piping. 设计一个系统能够read以及pipe用户privacy相关的consent。我答得不是很好

8, 重点是如何实现延迟支付
还有一个重点就是在peak traffic的时候 你design的系统哪里会出现 bottle neck

system design。 设计一个payment service，并且可以支持延迟支付，可以assume 已经有类似stripe 之类的service 
处理actual 的transaction，还要支持怎么cancel 一个scheduled 的payment。qps 要求5k，如何避免重复操作。
面试的时候先从api入手，定义interface。


- Design trading system to prevent frauds as much as possible. 面试官语速太快又很多aggressive
follow up questions，有点hold不住
- how to migrate online distributed cache system without downtime
- how to migrate online cache without downtime

System Design
- Processing payment holds
- Design a system for processing payment holds for Roblox platform
- Hold a variable amount of virtual money (Robux) to be paid to recipient after a designated (variable)
time. Example requests: Pay 100 Robux to User123 after 48 hours; Pay 300 Robux to User33 after 2
hours.
- Focus areas:
- 1. Interface of the system (how is your system exposed to consumers and why? There should be a
way to cancel hold before it has mat‍‍‍‍‌‌‍‌‌‌‍‌‍‌‌‍‍‍‍‍‍ ured)
- 2. Storage (what storage are you going to use and why?)
- 3. Processing holds (how are you going to make sure that holds are processed after designated
time?)
- payment hold/delayed queue. 因为需要做一些fraud detection之类的，平台想要延时付钱给游戏
的作者。所以会产生一些输入[{user1, pay amount:$100, time: 15:00}, {user2, pay amount:$50,
time: 16:00}...]。按照面试官的意思，要求是payment在指定时间的几分钟之内发生吧，如果
出错了要像个办法处理
- Design payment system
- 设计一个payment hold的系统。这个其他面筋也提到过，讲一下其他面筋都没有提到的问
题。第一：QPS 5K， 第二：这个系统需要直接cancel payment。这个就需要确定payment
hold API的返回值是什么，如果用了卡夫卡做缓冲会怎么样，NO SQL怎么做sharding等等，
这个地方我答的不太好，很可能就是挂在这里，希望可以帮到后来人。另外也问了一下
payment system怎么跟payment hold配合工作的，需要讲一下payment system的workflow和
DB。
- 设计一个delay transcation system，背景是他们自己的game platform里面的虚拟货币，要求用
户可以设定一个未来的时间来给另一个用户转特定数额的钱，并可以支持cancel还未发生的
transactions，可以assume有一个banking API可以call去真正执行transaction。
- Design a payment scheduling system. 主要要求是可以允许Roblox玩家说给另一个玩家转一定数
量的游戏币，不过要在指定是时间点转（比如3天后，2小时后之类的），然后不用考虑
payment system本身的设计，就假设有个现成的payment API。大方向上像个delayed job
scheduling system，不过有一些特别的细节：（1）发起转账的用户里面的钱得立马扣下；
（2）指定的未来时间可以是10几秒之后，所以定时polling的系统是不行的；（3）发给接收
方的钱的操作可能会有不可重试的错误，比如接收方账户因为用外挂被注销了什么的，所以
其实整个系统其实是个transaction系统，要考虑rollback，以及常见的WAL之类的手段来达到
durability要求。面试官还粗略问了一些API design（REST vs RPC），API security，
notification，idempotency（payment）相关的内容。

# https://www.1point3acres.com/bbs/thread-1091581-1-1.html








