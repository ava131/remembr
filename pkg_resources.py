class DistributionNotFound(Exception):
    pass
class MockDist:
    version = '2.4.0'
def get_distribution(name):
    return MockDist()
__version__ = '2.4.0'