import tcod
from tcod.context import Context

from engine import Engine
from game_map import GameMap
from input_handlers import EventDispatcher
from entity import Entity

def main() -> None: 
    screen_width = 80
    screen_height = 50
    
    map_width = 80
    map_height = 50
    
    tileset = tcod.tileset.load_tilesheet(
        "./python_roguelike/2424_tileset.png", 16, 16, tcod.tileset.CHARMAP_CP437
    )
    
    cp437_to_unicode = tcod.tileset.CHARMAP_CP437
    event_dispatcher = EventDispatcher()
    
    player = Entity(int(screen_width / 2), int(screen_height / 2), chr(cp437_to_unicode[1]), (255, 255, 255))
    npc = Entity(int(screen_width / 2 - 5), int(screen_height / 2), chr(cp437_to_unicode[2]), (255, 255, 0))
    entities = {npc, player}
    
    game_map = GameMap(map_width, map_height)
    
    engine = Engine(entities = entities, event_dispatcher = event_dispatcher, game_map = game_map, player = player)
    
    
    with tcod.context.new(
        columns=screen_width,
        rows=screen_height,
        tileset=tileset,
        title="Python Roguelike",
        vsync=True,
    )  as context:
        root_console = tcod.Console(screen_width, screen_height, order = "F")
        
        while True: 
            engine.render(console = root_console, context = context)
            events = tcod.event.wait()
            engine.handle_events(events)
            

if __name__ == "__main__":
    main()
        
    