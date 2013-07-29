from boundaryservice.throttle import AnonymousThrottle
from boundaryservice.resources import BoundarySetResource, BoundaryResource


class LATBoundarySetResource(BoundarySetResource):
    
    class Meta(BoundarySetResource.Meta):
        throttle = AnonymousThrottle(throttle_at=100) 


class LATBoundaryResource(BoundaryResource):
    
    class Meta(BoundaryResource.Meta):
        throttle = AnonymousThrottle(throttle_at=100)
