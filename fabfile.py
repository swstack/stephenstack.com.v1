from fabric.api import run, env, local, cd

env.hosts = ['stephenstack.com']
env.user = 'stephft5'
env.password = 'Baller1997!'

def deploy():
    try:
        run('rm -r ~/public_html/frontend')
    except:
        pass
    
    with cd('~/django_projects/SoftwareStack'):
        run('hg pull')
        run('hg update')
        run('cp -r frontend ~/public_html/frontend')