from streamer import controller_node


class ShakaPackagerController:
    def __init__(self, controller_node):
        self.controller = controller_node.ControllerNode()

    def create_vod(self, video):
        self.controller.start()


if __name__ == '__main__':
    controller = ShakaPackagerController(controller_node)

    print(controller.create_vod("dsd"))
