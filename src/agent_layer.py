class Agent:
    """代理类
    
    表示蜂群中的单个代理。
    """
    
    def __init__(self, name, role):
        """初始化代理
        
        Args:
            name: 代理名称
            role: 代理角色（如'Leader'或'Worker'）
        """
        self.name = name
        self.role = role
        
    def perform_task(self, task):
        """执行任务
        
        Args:
            task: 要执行的任务
            
        Returns:
            str: 任务执行结果描述
        """
        return f"{self.name} ({self.role}) 执行任务: {task}"

class SwarmLevel:
    """蜂群层级类
    
    管理特定层级的代理群。
    """
    
    def __init__(self, level_name):
        """初始化蜂群层级
        
        Args:
            level_name: 层级名称
        """
        self.level_name = level_name
        self.agents = []
        
    def add_agent(self, agent):
        """添加代理到当前层级
        
        Args:
            agent: 要添加的代理
        """
        self.agents.append(agent)
        
    def delegate_task(self, task):
        """委派任务给层级中的所有代理
        
        Args:
            task: 要委派的任务
            
        Returns:
            list: 所有代理的任务执行结果
        """
        return [agent.perform_task(task) for agent in self.agents]

class HierarchicalSwarm:
    """分层蜂群类
    
    实现分层蜂群结构的主要类。
    """
    
    def __init__(self):
        """初始化分层蜂群"""
        self.levels = {}
        
    def add_level(self, level_name):
        """添加新的层级
        
        Args:
            level_name: 层级名称
        """
        self.levels[level_name] = SwarmLevel(level_name)
        
    def add_agent_to_level(self, level_name, agent):
        """将代理添加到指定层级
        
        Args:
            level_name: 目标层级名称
            agent: 要添加的代理
        """
        if level_name in self.levels:
            self.levels[level_name].add_agent(agent)
        else:
            print(f"层级 {level_name} 不存在。")
            
    def delegate_task_to_level(self, level_name, task):
        """向指定层级委派任务
        
        Args:
            level_name: 目标层级名称
            task: 要委派的任务
            
        Returns:
            list: 任务执行结果，如果层级不存在则返回None
        """
        if level_name in self.levels:
            return self.levels[level_name].delegate_task(task)
        else:
            print(f"层级 {level_name} 不存在。")
            return None
