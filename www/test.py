import orm, asyncio
from model import User, Blog, Comment

@asyncio.coroutine
def test(loop):
    yield from orm.create_pool(loop=loop, user='root', password='password', db='awesome')
    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')
    yield from u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()