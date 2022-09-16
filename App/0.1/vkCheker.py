class VkChecker(object):
    def __init__(self, api):
        self.api = api
        self.groups = [
            ['kip_college', 931]
        ]

    def check_update(self):
        for lst in self.groups:
            try:
                if self.api.wall.get(domain=lst[0], v=5.92)['count'] != lst[1]:
                    print(f"New Post in group: https://vk.com/{lst[0]}")
                else:
                    print("No update")
            except:
                pass
