class SystemCheck:
    def __init__(self, content_checker, resource_checker, dependency_checker):
        self.content_checker = content_checker
        self.resource_checker = resource_checker
        self.dependency_checker = dependency_checker

    def perform_full_check(self):
        content_ok = self.content_checker.check_all()
        resources_ok = self.resource_checker.check_resources()
        dependencies_ok = self.dependency_checker.check_dependencies()

        if content_ok and resources_ok and dependencies_ok:
            return True, "All system components are healthy."
        else:
            report = {
                "content_check": content_ok,
                "resource_check": resources_ok,
                "dependency_check": dependencies_ok
            }
            return False, report