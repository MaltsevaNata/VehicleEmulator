from aiohttp_pydantic import PydanticView


class BaseView(PydanticView):
    def __init__(self, *args, **kwargs):
        super(BaseView, self).__init__(*args, **kwargs)
        self.storage = self.request.app["storage"]
