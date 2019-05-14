"""Helper functions for cloud components."""
from typing import Any, Dict

from aiohttp import web, payload


def aiohttp_serialize_response(response: web.Response) -> Dict[str, Any]:
    """Serialize an aiohttp response to a dictionary."""
    body = response.body

    if isinstance(body, payload.StringPayload):
        # pylint: disable=protected-access
        body = body._value.decode(body.encoding)
    else:
        raise ValueError("Unknown payload encoding")

    return {
        'status': response.status,
        'body': body,
        'headers': dict(response.headers),
    }
