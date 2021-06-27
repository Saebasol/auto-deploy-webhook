from sanic import Sanic

app = Sanic("server")

@app.post("deploy")
async def _deploy(request):
    ...
