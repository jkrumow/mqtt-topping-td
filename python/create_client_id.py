import uuid
import platform


def onTableChange(dat, _, __):
    app_id = dat[0, 0]
    hostname = platform.node()
    random_uuid = uuid.uuid4()
    short_uuid = str(random_uuid)[-8:]
    op('mqtt_client_id')[0, 0] = f"{app_id}-{hostname}-{short_uuid}"
