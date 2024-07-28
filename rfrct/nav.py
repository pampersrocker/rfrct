from extensions import nav

@nav.navigation()
def top_nav():
    return [
        nav.Item('Home', 'home.index'),
        nav.Item('Material', 'material.index'),
    ]