from extensions import nav
from flask_nav.elements import *
from flask_tabler.nav import TablerNav, User

@nav.navigation()
def top_nav():
    return TablerNav(
        "rfrct",
        [
            View('Home', 'home.index'),
            View('Material', 'material.index'),
        ],
        [
            User(
                [
                    # View('Profile', 'profile.index'),
                    # View('Settings', 'settings.index'),
                    View("Logout", "security.logout"),
                ],
                no_auth=View("Login", "security.login"),
            )
        ],
        show_theme_toggle=True,

    )
    
