from fabric.api import roles

from .commands import deploy, rollback
from .environment import testing, staging, live


@roles('frontend')
def deployfe():
    deploy()


@roles('frontend')
def rollbackfe():
    rollback()
