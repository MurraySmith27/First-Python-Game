
from GameObjects import GameObject
import pygame
import csv
import math


# Returns image of map
def MakeMap(map_csv_name, map_spritsheet_name, tile_size, tiles_per_row):
    csv_file = open(map_csv_name, "r")
    map = csv.reader(csv_file)
    map = [row for row in map]
    csv_file.close()
    map_size_tiles = (len(map[0]), len(map))
    map_size_pixels = (map_size_tiles[0] * tile_size, map_size_tiles[1] * tile_size)

    map_image = pygame.Surface([map_size_pixels[0], map_size_pixels[1]]).convert()

    map_spritesheet = pygame.image.load(map_spritsheet_name).convert_alpha()
    gameObjects = []
    for map_tile_y in range(0, map_size_tiles[1]):
        for map_tile_x in range(0, map_size_tiles[0]):
            tile_id = int(map[map_tile_y][map_tile_x])
            map_pixel_pos = (map_tile_x*tile_size, map_tile_y*tile_size)
            if tile_id < 0:
                continue
            spr_x = tile_size * (tile_id % tiles_per_row)
            spr_y = tile_size * math.floor(tile_id / tiles_per_row)
            #set all black pixels on the map_image to transparent when blitting
            map_image.set_colorkey((0,0,0))
            map_image.blit(map_spritesheet, map_pixel_pos, (spr_x, spr_y, tile_size, tile_size))
            go = GameObject(map_pixel_pos[0], map_pixel_pos[1], tile_size, tile_size)
            gameObjects.append(go)



    return map_image, gameObjects
