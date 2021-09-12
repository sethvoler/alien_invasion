class GameStats():
  """跟踪游戏的统计信息"""
  def __init__(self, ai_settings):
    self.ai_settings = ai_settings
    self.reset_stats()

    # 游戏启动时处于活动状态
    self.game_active = False
    # 在任何情况下都不应重置最高得分
    try:
      with open('high.txt', 'r', encoding='utf-8') as f:
        high_score = int(f.readline())
    except:
      self.high_score = 0
    else:
      if high_score:
        self.high_score = high_score
      else:
        self.high_score = 0
        

  def reset_stats(self):
    """初始化在游戏运行期间可能变化的统计信息""" 
    self.ships_left = self.ai_settings.ship_limit
    self.score = 0
    self.level = 1
