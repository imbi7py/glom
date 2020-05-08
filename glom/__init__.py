from pkg_resources import get_distribution

from glom.core import (glom,
                       Fill,
                       Auto,
                       register,
                       Glommer,
                       Call,
                       Invoke,
                       Spec,
                       Ref,
                       OMIT,  # backwards compat
                       SKIP,
                       STOP,
                       UP,
                       ROOT,
                       MODE,
                       Check,
                       Path,
                       Literal,
                       Coalesce,
                       Inspect,
                       GlomError,
                       BadSpec,
                       CheckError,
                       PathAccessError,
                       CoalesceError,
                       UnregisteredTarget,
                       T, S)
from glom.mutation import Assign, Delete, assign, delete, PathAssignError, PathDeleteError
from glom.reduction import Sum, Fold, Flatten, flatten, FoldError, Merge, merge
# there's no -ion word that really fits what "streaming" means.
# generation, production, iteration, all have more relevant meanings
# elsewhere. (maybe procrastination :P)
from glom.streaming import Iter

__version__ = get_distribution(dist="glom").version
