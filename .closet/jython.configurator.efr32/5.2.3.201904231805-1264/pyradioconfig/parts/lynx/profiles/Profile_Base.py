from pyradioconfig.parts.common.profiles.Profile_Base import *



class Profile_Base_Lynx(Profile_Base):

    """
    Init internal variables
    """
    def __init__(self):
        super(self.__class__, self).__init__()
        self._description = "Profile used for most phy's on EFR32xG22 parts"
        # TODO: confirm Lynx part is xG22
        self._family = "lynx"

