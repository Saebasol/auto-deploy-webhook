from asyncio.subprocess import PIPE, create_subprocess_shell

from sanic import Sanic


app = Sanic("server")

@app.get("deploy")
async def _deploy(request):
    proc = await create_subprocess_shell("ls", stdout=PIPE, stderr=PIPE)

    stdout, stderr = await proc.communicate()
    print(stdout)

    print(f"['ls' exited with {proc.returncode}]")
    if stdout:
        print(f"[stdout]\n{stdout.decode()}")
    if stderr:
        print(f"[stderr]\n{stderr.decode()}")


app.run()
