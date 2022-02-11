from typing import Optional, List

from pymongo import errors
from pydantic import PositiveInt
from aiohttp import web
from aiohttp_pydantic.oas.typing import r200

from views.base import BaseView
from models.component import Component


class ComponentsView(BaseView):
    async def get(self,
                  page_size: Optional[PositiveInt] = 50,
                  page_num: Optional[PositiveInt] = 1
                  ) -> r200[List[Component]]:
        """
        Get all components paginated by page_size
        Tags: components
        status codes:
            400: Invalid arguments in query string
            200: Success
        """
        try:
            data = await self.storage.get_list(page_size, page_num)
        except errors.ConnectionFailure:
            raise web.HTTPServiceUnavailable(reason='No connection to database')
        return web.json_response([doc for doc in data])
