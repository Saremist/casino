class OverWorkLimitError(Exception):
    def __init__(self, worker_name) -> None:
        super().__init__(f"{worker_name} can't work on over 2 projects")


class NoMenagerError(Exception):
    def __init__(self) -> None:
        super().__init__("There is no avaible menagers to be selected")


class NoDeveloperError(Exception):
    def __init__(self, language) -> None:
        super().__init__(
            f"There is no avaible developers using {language} language to be selected"
        )


class Menager:
    All_menagers = []

    def __init__(self, lname, experience: int, p_count: int) -> None:
        self.set_lname(lname)
        self.set_experience(experience)
        self.set_project_count(p_count)
        if not isinstance(self, Developer):
            Menager.All_menagers.append(self)

    def set_lname(self, lname):
        if lname == "":
            raise ValueError("Last name cannot be empty")
        self._lname = lname

    def set_experience(self, experience):
        if experience < 0:
            raise ValueError("Experience cannot be negative")
        self._experience = experience

    def set_project_count(self, p_count):
        if p_count > 2:
            raise OverWorkLimitError(self._lname)
        if p_count < 0:
            raise ValueError("Project count cannot be negative")
        self._project_count = p_count


class Developer(Menager):
    All_developers = []
    """
    menager with coding language
    """

    def __init__(
        self, lname: str, experience: int, p_count: int, language: str
    ) -> None:
        super().__init__(lname, experience, p_count)
        self.set_language(language)
        Developer.All_developers.append(self)

    def set_language(self, language):
        self._language = language

    pass


class Project:
    def __init__(self, name: str, lang_dev_dict: dict) -> None:
        self.set_name(name)
        self.set_dev_dict(lang_dev_dict)
        self._developer_list = self.find_developers()
        self._head_menager = self.find_menager()

    def __str__(self) -> str:
        introduce = f"it's {self._name} project here. {self._head_menager._lname} is my menager. Thease are my developers: "
        for dev in self._developer_list:
            introduce += "\n" + dev._lname
        return introduce

    def set_name(self, name):
        self._name = name

    def set_dev_dict(self, dev_dict):
        if isinstance(dev_dict, dict):
            self._dev_dict = dev_dict
        else:
            raise ValueError("Inproper developer dicionary format")

    def find_menager(self):
        for menager in Menager.All_menagers:
            if menager._project_count < 2:
                menager._project_count += 1
                return menager
        raise NoMenagerError

    def find_developers(self):
        developers = []
        for language in self._dev_dict:
            while self._dev_dict[language] != 0:
                developers.append(self.find_one_developer(language))
                self._dev_dict[language] -= 1
        return developers

    def find_one_developer(self, language) -> Developer:
        for developer in Developer.All_developers:
            if developer._language == language:
                if developer._project_count < 2:
                    developer.set_project_count((developer._project_count + 1))
                return developer
        raise NoDeveloperError(language)


if __name__ == "__main__":
    King = Menager("King", 5, 0)
    Me = Developer("Milan Wróblewski", 10, 0, "python")
    first_project = Project("First", {"python": 1})
    print(str(first_project))
