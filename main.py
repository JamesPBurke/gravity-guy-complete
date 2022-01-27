def on_a_pressed():
    if mySprite.is_hitting_tile(CollisionDirection.BOTTOM):
        mySprite.vy = -200
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_left_pressed():
    pass
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_right_pressed():
    pass
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

mySprite: Sprite = None
mySprite = sprites.create(img("""
        . . . . . . f f f f . . . . . . 
            . . . . f f f 2 2 f f f . . . . 
            . . . f f f 2 2 2 2 f f f . . . 
            . . f f f e e e e e e f f f . . 
            . . f f e 2 2 2 2 2 2 e e f . . 
            . . f e 2 f f f f f f 2 e f . . 
            . . f f f f e e e e f f f f . . 
            . f f e f b f 4 4 f b f e f f . 
            . f e e 4 1 f d d f 1 4 e e f . 
            . . f e e d d d d d d e e f . . 
            . . . f e e 4 4 4 4 e e f . . . 
            . . e 4 f 2 2 2 2 2 2 f 4 e . . 
            . . 4 d f 2 2 2 2 2 2 f d 4 . . 
            . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
            . . . . . f f f f f f . . . . . 
            . . . . . f f . . f f . . . . .
    """),
    SpriteKind.player)
tiles.set_tilemap(tilemap("""
    level1
"""))
movespeed = 80
mySprite.ay = 400
mySprite.fx += 100
scene.camera_follow_sprite(mySprite)
animating = 'none'

def on_on_update():
    global animating
    if controller.left.is_pressed():
        mySprite.set_image(img("""
            . . . . . . . . . . . . . . . . 
                        . . . . . f f f f f f . . . . . 
                        . . . . f 2 f e e e e f f . . . 
                        . . . f 2 2 2 f e e e e f f . . 
                        . . . f e e e e f f e e e f . . 
                        . . f e 2 2 2 2 e e f f f f . . 
                        . . f 2 e f f f f 2 2 2 e f . . 
                        . . f f f e e e f f f f f f f . 
                        . . f e e 4 4 f b e 4 4 e f f . 
                        . . . f e d d f 1 4 d 4 e e f . 
                        . . . . f d d d e e e e e f . . 
                        . . . . f e 4 e d d 4 f . . . . 
                        . . . . f 2 2 e d d e f . . . . 
                        . . . f f 5 5 f e e f f f . . . 
                        . . . f f f f f f f f f f . . . 
                        . . . . f f f . . . f f . . . .
        """))
        if abs(mySprite.vx) < 50:
            mySprite.vx = movespeed * -1
    elif controller.right.is_pressed():
        if animating != 'right':
            animation.run_image_animation(mySprite,
                [img("""
                        . . . . . . f f f f f f . . . . 
                                        . . . . f f e e e e f 2 f . . . 
                                        . . . f f e e e e f 2 2 2 f . . 
                                        . . . f e e e f f e e e e f . . 
                                        . . . f f f f e e 2 2 2 2 e f . 
                                        . . . f e 2 2 2 f f f f e 2 f . 
                                        . . f f f f f f f e e e f f f . 
                                        . . f f e 4 4 e b f 4 4 e e f . 
                                        . . f e e 4 d 4 1 f d d e f . . 
                                        . . . f e e e 4 d d d d f . . . 
                                        . . . . f f e e 4 4 4 e f . . . 
                                        . . . . . 4 d d e 2 2 2 f . . . 
                                        . . . . . e d d e 2 2 2 f . . . 
                                        . . . . . f e e f 4 5 5 f . . . 
                                        . . . . . . f f f f f f . . . . 
                                        . . . . . . . f f f . . . . . .
                    """),
                    img("""
                        . . . . . . . . . . . . . . . . 
                                        . . . . . . f f f f f f . . . . 
                                        . . . . f f e e e e f 2 f . . . 
                                        . . . f f e e e e f 2 2 2 f . . 
                                        . . . f e e e f f e e e e f . . 
                                        . . . f f f f e e 2 2 2 2 e f . 
                                        . . . f e 2 2 2 f f f f e 2 f . 
                                        . . f f f f f f f e e e f f f . 
                                        . . f f e 4 4 e b f 4 4 e e f . 
                                        . . f e e 4 d 4 1 f d d e f . . 
                                        . . . f e e e e e d d d f . . . 
                                        . . . . . f 4 d d e 4 e f . . . 
                                        . . . . . f e d d e 2 2 f . . . 
                                        . . . . f f f e e f 5 5 f f . . 
                                        . . . . f f f f f f f f f f . . 
                                        . . . . . f f . . . f f f . . .
                    """),
                    img("""
                        . . . . . . f f f f f f . . . . 
                                        . . . . f f e e e e f 2 f . . . 
                                        . . . f f e e e e f 2 2 2 f . . 
                                        . . . f e e e f f e e e e f . . 
                                        . . . f f f f e e 2 2 2 2 e f . 
                                        . . . f e 2 2 2 f f f f e 2 f . 
                                        . . f f f f f f f e e e f f f . 
                                        . . f f e 4 4 e b f 4 4 e e f . 
                                        . . f e e 4 d 4 1 f d d e f . . 
                                        . . . f e e e 4 d d d d f . . . 
                                        . . . . f f e e 4 4 4 e f . . . 
                                        . . . . . 4 d d e 2 2 2 f . . . 
                                        . . . . . e d d e 2 2 2 f . . . 
                                        . . . . . f e e f 4 5 5 f . . . 
                                        . . . . . . f f f f f f . . . . 
                                        . . . . . . . f f f . . . . . .
                    """),
                    img("""
                        . . . . . . . . . . . . . . . . 
                                        . . . . . . f f f f f f . . . . 
                                        . . . . f f e e e e f 2 f . . . 
                                        . . . f f e e e e f 2 2 2 f . . 
                                        . . . f e e e f f e e e e f . . 
                                        . . . f f f f e e 2 2 2 2 e f . 
                                        . . . f e 2 2 2 f f f f e 2 f . 
                                        . . f f f f f f f e e e f f f . 
                                        . . f f e 4 4 e b f 4 4 e e f . 
                                        . . f e e 4 d 4 1 f d d e f . . 
                                        . . . f e e e 4 d d d d f . . . 
                                        . . . . 4 d d e 4 4 4 e f . . . 
                                        . . . . e d d e 2 2 2 2 f . . . 
                                        . . . . f e e f 4 4 5 5 f f . . 
                                        . . . . f f f f f f f f f f . . 
                                        . . . . . f f . . . f f f . . .
                    """)],
                500,
                True)
        if abs(mySprite.vx) < 50:
            mySprite.vx = movespeed
    elif mySprite.vx < 2:
        mySprite.set_image(img("""
            . . . . . . f f f f . . . . . . 
                        . . . . f f f 2 2 f f f . . . . 
                        . . . f f f 2 2 2 2 f f f . . . 
                        . . f f f e e e e e e f f f . . 
                        . . f f e 2 2 2 2 2 2 e e f . . 
                        . . f e 2 f f f f f f 2 e f . . 
                        . . f f f f e e e e f f f f . . 
                        . f f e f b f 4 4 f b f e f f . 
                        . f e e 4 1 f d d f 1 4 e e f . 
                        . . f e e d d d d d d e e f . . 
                        . . . f e e 4 4 4 4 e e f . . . 
                        . . e 4 f 2 2 2 2 2 2 f 4 e . . 
                        . . 4 d f 2 2 2 2 2 2 f d 4 . . 
                        . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
                        . . . . . f f f f f f . . . . . 
                        . . . . . f f . . f f . . . . .
        """))
    else:
        pass
game.on_update(on_on_update)
