Subject: 大数据开发面试复习资料 - 核心技术栈详解
To: nohotnnn@gmail.com

=====================================================================
         大数据开发面试复习资料 - 核心技术栈详解
=====================================================================

你好！这是一份为你整理的大数据开发面试复习资料，包含核心技术栈的详细知识点和优质学习链接。

=====================================================================
                    一、Hadoop 生态
=====================================================================

【HDFS 分布式文件系统】

架构核心：
- NameNode：元数据管理（fsimage + editlog），负责文件元数据操作
- DataNode：存储实际数据块，负责读写请求
- Secondary NameNode：定期合并 edits 和 fsimage

读写流程（必须掌握）：
1. 客户端请求 NameNode 获取文件块位置列表
2. NameNode 返回 DataNode 列表（就近原则）
3. 客户端直接与 DataNode 通信读写数据
4. DataNode 写入完成后反馈成功给 NameNode

数据块副本存储策略：
- 第一个副本：客户端同节点（本地）
- 第二个副本：不同机架的节点
- 第三个副本：同机架不同节点

参考文档：https://hadoop.apache.org/docs/current/

-----------------------------------------------------------------

【MapReduce 分布式计算】

工作流程：
1. InputFormat → 读取数据，生成 split
2. Map 阶段：逐行处理，输出 (key, value) 对
3. Shuffle 阶段（核心）：Partition → Sort → Combine → Merge
4. Reduce 阶段：聚合相同 key 的值
5. OutputFormat：写入 HDFS

Shuffle 详解：
- Map 端：先在内存缓冲区（默认100MB）处理，达到阈值溢写到磁盘
- 排序：按 key 排序，可选 Combiner 本地聚合
- Reduce 端：多个 Map 节点的数据通过 HTTP 拉取到本地
- 合并：相同 partition 的文件合并为一个

面试常问题：
- Map 端溢写触发条件
- 如何避免数据倾斜
- Combiner 和 Partitioner 的区别

-----------------------------------------------------------------

【YARN 资源调度】

架构：
- ResourceManager：全局资源管理器（Scheduler + ApplicationsManager）
- NodeManager：每个节点上的资源管理
- ApplicationMaster：每个应用的管理者
- Container：资源抽象（CPU + 内存）

调度器：
- FIFO Scheduler：单队列，先进先出
- Capacity Scheduler：多队列，资源预留
- Fair Scheduler：多队列，动态分配，资源公平

=====================================================================
                    二、Spark 核心
=====================================================================

【RDD (Resilient Distributed Dataset)】

五大特性：
1. 分区列表
2. 计算函数（每个分区计算逻辑）
3. 依赖关系（父 RDD）
4. 分区器（可选，kv 类型）
5. 优先位置（可选）

创建方式：
- 并行集合：sc.parallelize()
- 外部数据：sc.textFile()
- 已有 RDD 转换

Transformation（转换，懒执行）：
- map, flatMap, filter, distinct
- reduceByKey, groupByKey, sortByKey
- join, cogroup, union, intersection

Action（行动，立即执行）：
- collect, count, first, take
- reduce, aggregate, fold
- saveAsTextFile, foreach

面试必问题：
- RDD 窄依赖 vs 宽依赖（划分 Stage 的依据）
- DAG 如何划分 Stage（遇到 Shuffle 就划分）
- 血缘关系与容错机制

-----------------------------------------------------------------

【DataFrame & Dataset】

- DataFrame：Schema + RDD，类似关系型数据库表
- Dataset：强类型的 DataFrame（Scala/Java）

Spark SQL 执行流程：
1. 解析 SQL，生成 Unresolved Logical Plan
2. 分析阶段，绑定列和表（Catalog）
3. 优化阶段（Catalyst 优化器）
4. 物理计划生成
5. 执行

-----------------------------------------------------------------

【内存管理】

Spark 1.6 前：静态内存管理
Spark 2.0+：统一内存管理（堆内 + 堆外）

内存区域：
- Execution：Shuffle、排序、缓存
- Storage：RDD 缓存、广播变量
- User：用户代码
- Reserved：系统预留（300MB）

内存溢出常见原因：
- 无限递归导致栈溢出
- 数据量太大，collect 到 driver
- Shuffle 文件过多，内存不足

-----------------------------------------------------------------

【Shuffle 优化】

常见优化手段：
- 减少 Shuffle 数据量（map-side 预聚合）
- 合理设置分区数（避免太小或太大）
- 使用 HashShuffleManager（Spark 1.2 前）
- 使用 SortShuffleManager（默认）
- 启用 BypassMergeSortShuffle（小数据量）
- 增加 Shuffle 内存

=====================================================================
                    三、Kafka 消息队列
=====================================================================

【核心概念】

- Broker：Kafka 服务节点
- Topic：消息主题
- Partition：分区（并行消费，提高吞吐）
- Replication：副本（高可用）
- Producer：生产者
- Consumer：消费者
- Consumer Group：消费组（同一组内消息只消费一次）

-----------------------------------------------------------------

【架构原理】

ISR（In-Sync Replicas）机制：
- 与 Leader 保持同步的副本集合
- 通过 replica.lag.time.max.ms 参数控制同步超时

消息顺序性：
- 单分区：保证顺序
- 多分区：跨分区不保证顺序
- 解决：key 相同发送到同一分区

Exactly Once 语义：
- 幂等性：enable.idempotence=true
- 事务：事务API（原子写入多分区）

-----------------------------------------------------------------

【常见面试题】

- Kafka 消息丢失场景及如何避免
- Kafka 消费顺序性如何保证
- 分区再均衡（Rebalance）机制
- 如何查看消费滞后（Lag）
- 高吞吐量原因（顺序写、零拷贝、批量处理）

=====================================================================
                    四、Flink 流处理
=====================================================================

【核心概念】

API 层级（从低到高）：
1. ProcessFunction：最低层，状态 + 时间
2. DataStream API：核心 API
3. Table API：声明式 DSL
4. SQL：最高层

-----------------------------------------------------------------

【窗口函数】

滚动窗口（Tumbling）：不重叠
- TumblingEventTimeWindow

滑动窗口（Sliding）：有重叠
- SlidingEventTimeWindow

会话窗口（Session）：按活动间隙划分
- EventTimeSessionWindows

-----------------------------------------------------------------

【时间语义】

Event Time（事件时间）：
- 数据本身携带的时间戳
- 需要 Watermark 解决乱序
- 迟到数据处理：allowedLateness, sideOutputLateData

Processing Time（处理时间）：
- 机器本地时间
- 简单，但结果不确定

Watermark 机制：
- 乱序容忍度
- 触发窗口计算的条件
- 常见策略：单调递增、周期性、惩罚性

-----------------------------------------------------------------

【状态管理】

Keyed State：
- ValueState：单值状态
- ListState：列表状态
- MapState：映射状态
- ReducingState：聚合状态

Operator State：
- ListState：列表状态
- UnionListState：广播状态
- BroadcastState：广播状态

状态后端：
- HashMapStateBackend：内存，状态小
- EmbeddedRocksDBStateBackend：RocksDB，状态大

-----------------------------------------------------------------

【Checkpoints & Savepoints】

Checkpoint：
- 自动触发，JobManager 协调
- 增量 vs 全量
- 轻量级，恢复快

Savepoint：
- 手动触发，持久化存储
- 用于升级、迁移

Barrier 对齐机制：
- Exactly Once 语义需要对齐
- At Least Once 可以不对齐

=====================================================================
                    五、Hive 数据仓库
=====================================================================

【架构】

- Driver：JDBC/ODBC 接口
- Compiler：SQL 解析，生成 AST
- Optimizer：查询优化
- Executor：执行计划

执行流程：
1. SQL 解析 → AST
2. 语义分析 → Query Block
3. 生成逻辑计划 → Operator Tree
4. 优化逻辑计划
5. 生成物理计划 → Task Tree
6. 执行

-----------------------------------------------------------------

【存储格式】

行式存储：TextFile, SequenceFile
列式存储：ORC, Parquet（推荐）

ORC 特点：
- 按列压缩
- 内置索引（Bloom Filter, Min/Max）
- 支持 ACID

Parquet 特点：
- 嵌套结构支持
- 跨语言友好
- 列式压缩

-----------------------------------------------------------------

【优化技巧】

SQL 优化：
- 分区裁剪
- 桶表 + JOIN 优化
- 避免笛卡尔积
- 合理设置 Map/Reduce 数
- 启用向量化引擎（Vectorized Query Execution）
- CBO 优化（Cost-Based Optimizer）

数据倾斜：
- 加盐 key
- 手动打散大 key
- 调整 join 策略

=====================================================================
                    六、HBase 分布式数据库
=====================================================================

【架构】

- HMaster：元数据管理、负载均衡
- RegionServer：负责数据读写
- Region：表的数据范围
- MemStore：写缓存
- StoreFile：HFile，持久化存储

读写流程：
- 写：先写 WAL，再写 MemStore，达到阈值 flush 成 HFile
- 读：先查 MemStore，未命中再查 BlockCache，最后查 HFile

-----------------------------------------------------------------

【RowKey 设计】

原则：
- 散列：避免热点
- 长度：越短越好（不超过 100 字节）
- 唯一：唯一标识

设计模式：
- 盐值加盐
- 哈希
- 倒序
- 组合字段

=====================================================================
                    七、Java 基础（面试必考）
=====================================================================

【集合源码】

HashMap（JDK 8+）：
- 数组 + 链表 + 红黑树
- 链表转红黑树阈值：8
- 红黑树转链表阈值：6
- 扩容因子：0.75
- 容量必须是 2 的幂

ConcurrentHashMap：
- JDK 7：分段锁
- JDK 8：CAS + synchronized + 红黑树

ArrayList：
- 数组实现
- 扩容：1.5 倍
- 不是线程安全

-----------------------------------------------------------------

【JVM 内存模型】

分区：
- 堆：对象分配（Young Gen + Old Gen）
- 方法区：类信息、常量、静态变量
- 虚拟机栈：方法调用
- 本地方法栈：Native 方法
- 程序计数器：当前线程执行位置

垃圾回收算法：
- 标记-清除
- 标记-整理
- 复制算法（Young 区）

常见垃圾收集器：
- Serial：单线程
- Parallel：多线程，关注吞吐量
- CMS：并发标记清除
- G1：区域化垃圾收集器
- ZGC / Shenandoah：低延迟

-----------------------------------------------------------------

【多线程】

ThreadPoolExecutor：
- 核心线程数 + 最大线程数
- 队列 + 拒绝策略
- 线程复用原理

AQS（AbstractQueuedSynchronizer）：
- CAS + volatile
- 独占模式 vs 共享模式
- ReentrantLock, CountDownLatch, CyclicBarrier

=====================================================================
                    八、系统设计
=====================================================================

【数据仓库分层】

- ODS（Operational Data Store）：原始数据层
- DWD（Data Warehouse Detail）：明细数据层
- DWS（Data Warehouse Service）：汇总数据层
- ADS（Application Data Service）：应用数据层

-----------------------------------------------------------------

【离线 vs 实时数仓】

离线数仓：
- T+1 批处理
- 稳定、准确
- Hive, Spark SQL

实时数仓：
- 实时流处理
- 延迟秒级/分钟级
- Flink, Kafka, ClickHouse

-----------------------------------------------------------------

【CDC (Change Data Capture)】

技术方案：
- Binlog 监听（MySQL）
- Debezium + Kafka
- Canal + MQ

=====================================================================
                    九、优质学习资源
=====================================================================

官方文档（最权威）：
- Spark: https://spark.apache.org/docs/latest/
- Flink: https://nightlies.apache.org/flink/flink-docs-stable/
- Kafka: https://kafka.apache.org/documentation/
- Hadoop: https://hadoop.apache.org/docs/current/
- Hive: https://hive.apache.org/docs/

视频教程：
- 尚硅谷大数据技术系列（B站）
- 极客时间《从0开始学大数据》

=====================================================================
                    十、常见面试题汇总
=====================================================================

1. Spark Shuffle 原理及优化方案
2. Kafka 如何保证消息不丢失/不重复
3. 数据倾斜原因及解决方案
4. Flink Checkpoint 原理
5. HDFS 读写流程
6. Spark 内存管理机制
7. Kafka 分区再均衡
8. 如何处理乱序消息
9. MapReduce Shuffle 过程
10. HBase RowKey 设计原则

=====================================================================

祝你面试顺利！🎉

如果需要更具体的内容，可以随时告诉我。

---
Generated by Ovo 🤖
