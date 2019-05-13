import FeatureEngineering as fe

class Device(object):
    def __init__(self):
        self.packet_info = []
        self.feature_data = []

    def append_packet_info(self, packet_info):
        temp = fe.PacketInfo(packet_info)
        self.packet_info.append(temp)
    
    def append_feature_data(self, feature_data):
        temp = fe.FeatureData(feature_data)
        self.feature_data.append(temp)

    # count number of destinations
    def count_endpoint(self):
        endpoint = []
        for value in self.packet_info:
            endpoint.append(value.destination)
        endpoint = list(set(endpoint)) # delete overlapped data

        return len(endpoint)

