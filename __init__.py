import Live
import _Framework.Capabilities as caps
from .Push2UserModeScript import Push2UserModeScript

def get_capabilities():
    return {caps.CONTROLLER_ID_KEY: caps.controller_id(vendor_id=10626, product_ids=[
            6503], model_name='Ableton Push 2'),
            caps.PORTS_KEY: [
                caps.inport(props=[]),
                caps.inport(props=[caps.NOTES_CC, caps.SCRIPT, caps.REMOTE]),
                caps.outport(props=[]),
                caps.outport(props=[caps.NOTES_CC, caps.SCRIPT, caps.REMOTE])]}

def create_instance(c_instance):

    return Push2UserModeScript(c_instance)