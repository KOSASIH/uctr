import logging

from .regulator.activities import manage_activities
from .regulator.compliance import ensure_compliance
from .manager.system import manage_system
from .manager.reporting import generate_reports

logger = logging.getLogger(__name__)

def main():
    """
    Main function for UCTR system.
    """
    manage_activities()
    ensure_compliance()
    manage_system()
    generate_reports()

if __name__ == "__main__":
    main()
