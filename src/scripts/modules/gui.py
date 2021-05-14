import pygame

class center_constraint():
    pass

class aspect_constraint():
    def __init__(self, aspect_ratio) -> None:
        self.value = aspect_ratio

class percentage_constraint():
    def __init__(self, percentage):
        self.value = percentage

class pixel_constraint():
    def __init__(self, pixel):
        self.value = pixel

class gui_rect:
    x_constraint = None
    y_constraint = None
    width_constraint = None
    height_constraint = None

    x = 0
    y = 0

    tween = False
    tween_x = 0
    tween_y = 0
    tween_mult = 0

    tween_s = False
    tween_width = 0
    tween_height = 0
    tween_s_mult = 0

    width = 0
    height = 0

    border_radius = 0
    outline = 0

    color = (0, 0, 0)

    parent = None

    ## Set Constraints

    # Position Constraints

    def set_x_constraint(self, x_constraint):
        self.x_constraint = x_constraint

    def set_y_constraint(self, y_constraint):
        self.y_constraint = y_constraint

    # Size Constraints

    def set_width_constraint(self, width_constraint):
        self.width_constraint = width_constraint

    def set_height_constraint(self, height_constraint):
        self.height_constraint = height_constraint

    # Misc to rect

    def set_border_radius(self, radius):
        self.border_radius = radius

    def set_outline_radius(self, outline):
        self.outline = outline

    def set_draw_color(self, rgb):
        self.color = rgb

    # Tools

    def is_touching_mouse(self):
        mx, my = pygame.mouse.get_pos()
        if self.game.math.in_rect(mx, my, self.x, self.y , self.width, self.height):
            return True
        return False

    def tween_to(self, x, y, mult):
        self.tween = True
        self.tween_x = x
        self.tween_y = y
        self.tween_mult = mult

    def tween_size(self, width, height, mult):
        self.tween_s = True
        self.tween_width = width
        self.tween_height = height
        self.tween_s_mult = mult

    def __init__(self, game) -> None:
        self.game = game
        self.visible = True

    ## Update thingy

    def update(self):

        ## Set Position thing

        if not self.tween:
            # Set X Constraints

            if self.x_constraint != None:
                class_use = type(self.x_constraint)
                if self.parent == None:
                    if class_use == center_constraint:
                        self.x = self.game.renderer.get_screen_size()[0] / 2 - (int(self.width) / 2)
                    if class_use == percentage_constraint:
                        self.x = self.game.renderer.get_screen_size()[0] * self.x_constraint.value
                    if class_use == pixel_constraint:
                        self.x = self.x_constraint.value
                else:
                    if class_use == center_constraint:
                        self.x = self.parent.x + (self.parent.width / 2) - (int(self.width) / 2)
                    if class_use == percentage_constraint:
                        self.x = self.parent.x + (self.parent.width * self.x_constraint.value)
                    if class_use == pixel_constraint:
                        self.x = self.parent.x + self.x_constraint.value

            # Set Y Constraints

            if self.y_constraint != None:
                class_use = type(self.y_constraint)
                if self.parent == None:
                    if class_use == center_constraint:
                        self.y = self.game.renderer.get_screen_size()[1] / 2 - (int(self.height) / 2)
                    if class_use == percentage_constraint:
                        self.y = self.game.renderer.get_screen_size()[1] * self.y_constraint.value
                    if class_use == pixel_constraint:
                        self.y = self.y_constraint.value
                else:
                    if class_use == center_constraint:
                        self.y = self.parent.y + (self.parent.height / 2) - (int(self.height) / 2)
                    if class_use == percentage_constraint:
                        self.y = self.parent.y + (self.parent.height * self.y_constraint.value)
                    if class_use == pixel_constraint:
                        self.y = self.parent.y + self.y_constraint.value

        ## Set size thingy

        if not self.tween_s:

            # Set Width Constraints

            if self.width_constraint != None:
                class_use = type(self.width_constraint)
                if self.parent == None:
                    if class_use == percentage_constraint:
                        self.width = self.game.renderer.get_screen_size()[0] * self.width_constraint.value
                    if class_use == aspect_constraint:
                        self.width = self.height * self.width_constraint.value
                    if class_use == pixel_constraint:
                        self.width = self.width_constraint.value
                else:
                    if class_use == percentage_constraint:
                        self.width = self.parent.width * self.width_constraint.value
                    if class_use == aspect_constraint:
                        self.width = self.height * self.width_constraint.value
                    if class_use == pixel_constraint:
                        self.width = self.width_constraint.value

            # Set Height Constraints

            if self.height_constraint != None:
                class_use = type(self.height_constraint)
                if self.parent == None: 
                    if class_use == percentage_constraint:
                        self.height = self.game.renderer.get_screen_size()[1] * self.height_constraint.value
                    if class_use == aspect_constraint:
                        self.height = self.width * self.height_constraint.value
                    if class_use == pixel_constraint:
                        self.height = self.height_constraint.value
                else:
                    if class_use == percentage_constraint:
                        self.height = self.parent.height * self.height_constraint.value
                    if class_use == aspect_constraint:
                        self.height = self.width * self.height_constraint.value()
                    if class_use == pixel_constraint:
                        self.height = self.height_constraint.value

        # Tween Position

        if self.tween:
            tmp_x = 0
            tmp_y = 0
            class_use = type(self.tween_x)
            if self.parent == None:
                if class_use == center_constraint:
                    tmp_x = self.game.renderer.get_screen_size()[0] / 2 - (int(self.width) / 2)
                if class_use == percentage_constraint:
                    tmp_x = self.game.renderer.get_screen_size()[0] * self.tween_x.value
                if class_use == pixel_constraint:
                    tmp_x = self.tween_x.value
            else:
                if class_use == center_constraint:
                    tmp_x = self.parent.x + (self.parent.width / 2) - (int(self.width) / 2)
                if class_use == percentage_constraint:
                    tmp_x = self.parent.x + (self.parent.width * self.tween_x.value)
                if class_use == pixel_constraint:
                    tmp_x = self.parent.x + self.tween_x.value

            class_use = type(self.tween_y)
            if self.parent == None:
                if class_use == center_constraint:
                    tmp_y = self.game.renderer.get_screen_size()[1] / 2 - (int(self.height) / 2)
                if class_use == percentage_constraint:
                    tmp_y = self.game.renderer.get_screen_size()[1] * self.tween_y.value
                if class_use == pixel_constraint:
                    tmp_y = self.tween_y.value
            else:
                if class_use == center_constraint:
                    tmp_y = self.parent.y + (self.parent.height / 2) - (int(self.height) / 2)
                if class_use == percentage_constraint:
                    tmp_y = self.parent.y + (self.parent.height * self.tween_y.value)
                if class_use == pixel_constraint:
                    tmp_y = self.parent.y + self.tween_y.value

            self.x += (tmp_x - self.x) / ((self.tween_mult * self.game.delta_time) * 600)
            self.y += (tmp_y - self.y) / ((self.tween_mult * self.game.delta_time) * 600) 
            if int(self.x) == int(tmp_y) and int(self.y) and int(tmp_y):
                self.tween = False
                self.x_constraint = self.tween_x
                self.y_constraint = self.tween_y

        # Tween Size

        if self.tween_s:
            tmp_width = 0
            tmp_height = 0
            class_use = type(self.tween_width)
            if self.parent == None:
                if class_use == percentage_constraint:
                    tmp_width = self.game.renderer.get_screen_size()[0] * self.tween_width.value
                if class_use == aspect_constraint:
                    tmp_width = tmp_height
                if class_use == pixel_constraint:
                    tmp_width = self.tween_width.value
            else:
                if class_use == percentage_constraint:
                    tmp_width = self.parent.width * self.tween_width.value
                if class_use == aspect_constraint:
                    tmp_width = tmp_height
                if class_use == pixel_constraint:
                    tmp_width = self.tween_width.value

            class_use = type(self.tween_height)
            if self.parent == None: 
                if class_use == percentage_constraint:
                    tmp_height = self.game.renderer.get_screen_size()[1] * self.tween_height.value
                if class_use == aspect_constraint:
                    tmp_height = tmp_width
                if class_use == pixel_constraint:
                    tmp_height = self.tmp_height.value
            else:
                if class_use == percentage_constraint:
                    tmp_height = self.parent.height * self.tmp_height.value
                if class_use == aspect_constraint:
                    tmp_height = tmp_width
                if class_use == pixel_constraint:
                    tmp_height = self.tmp_height.value
                    
            self.width += (tmp_width - self.width) / ((self.tween_s_mult * self.game.delta_time) * 600)
            self.height += (tmp_height - self.height) / ((self.tween_s_mult * self.game.delta_time) * 600) 
            if int(self.width) == int(tmp_width) and int(self.height) and int(tmp_height):
                self.tween_s = False
                self.width_constraint = self.tween_width
                self.height_constraint = self.tween_height

    def render(self):
        if self.visible:
            pygame.draw.rect(self.game.renderer.screen, self.color, ((self.x, self.y), (self.width, self.height)), self.outline, self.border_radius)
        
class gui_toggle_button:
    def __init__(self, game) -> None:
        self.game = game
        self.rect = gui_rect(game)
    
        self.hover = False
        self.toggled = False

    def update(self):
        self.rect.update()
        if self.rect.is_touching_mouse():
            self.hover = True
        else:
            self.hover = False

        if self.hover and self.game.input.is_mouse_button_just_pressed():
            self.toggled = not self.toggled

    def render(self):
        self.rect.render()

class gui_press_button:
    def __init__(self, game) -> None:
        self.game = game
        self.rect = gui_rect(game)
    
        self.hover = False
        self.pressed = False

    def update(self):
        self.rect.update()
        if self.rect.is_touching_mouse():
            self.hover = True
        else:
            self.hover = False

        if self.hover and self.game.input.is_mouse_button_pressed():
            self.pressed = True
        else:
            self.pressed = False

    def render(self):
        self.rect.render()

class gui_slider:
    def __init__(self, game, val_start, val_end) -> None:
        self.game = game
        self.slider_body = gui_rect(game)
        self.slider_head = gui_rect(game)

        self.value = 0
        self.value_range = (val_start, val_end)

    def update(self):
        self.slider_body.update()
        self.slider_head.update()

        slider_bigger_bounding_box = ((self.slider_body.x, self.slider_body.y - 10), (self.slider_body.width, self.slider_body.height + 30))

        self.slider_head.x = max(self.slider_body.x, min(self.slider_head.x, self.slider_body.x + self.slider_body.width))

        self.value = (self.slider_head.x - self.slider_body.x) / (self.slider_body.width / self.value_range[1]) * 1.06

        mx, my = pygame.mouse.get_pos()
        if self.game.math.in_rect(mx, my, slider_bigger_bounding_box[0][0], slider_bigger_bounding_box[0][1], slider_bigger_bounding_box[1][0], slider_bigger_bounding_box[1][1]) and self.game.input.is_mouse_button_pressed():
            self.slider_head.tween_to(pixel_constraint(mx - self.slider_head.parent.x - self.slider_head.width / 2), center_constraint(), 12)

    def render(self):
        self.slider_body.render()
        self.slider_head.render()