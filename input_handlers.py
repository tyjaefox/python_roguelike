from typing import Optional
import tcod.event
from actions import Action, EscapeAction, MovementAction


class EventDispatcher: 
  
  def handle_event(self, event: tcod.event.Event) -> Optional[Action]:
    
    if isinstance(event, tcod.event.Quit):
        return self.ev_quit(event)
    
    elif isinstance(event, tcod.event.KeyDown):
        return self.ev_keydown(event)
    
    return None
  
  
  
  def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
      raise SystemExit()
  
  def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
      
      action: Optional[Action] = None
      key = event.sym
      
      if key == tcod.event.K_UP: 
          action = MovementAction(dx = 0, dy = -1)
          
      elif key == tcod.event.K_DOWN:
          action = MovementAction(dx = 0, dy = 1)
          
      elif key == tcod.event.K_LEFT:
          action = MovementAction(dx = -1, dy = 0)
          
      elif key == tcod.event.K_RIGHT:
          action = MovementAction(dx = 1, dy = 0)
          
          
      elif key == tcod.event.K_ESCAPE:
          action = EscapeAction()
          
      return action
    
    
    
      
    
    
    
    
        

