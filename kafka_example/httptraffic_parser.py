# -*- coding: utf-8 -*-

class HttpTraffic:

    def __init__(self):
        self.method = None
        self.url = None
        self.headers = {}
        self.body = None
        self.response_body = None
        self.server = None
        self.port = None

    def _parse_kafka_first_header(self, kafka_raw_msg_header):
        headers = kafka_raw_msg_header.split("\n")
        parsed_method_url = headers[1].split(" ")
        self.method, self.url = parsed_method_url[0], parsed_method_url[1]
        for i in range(2, len(headers)):
            parsed_header = headers[i].split(":")
            if parsed_header[0].find("Host") >= 0:  ## parse host
                self.server = parsed_header[1]
                self.port = parsed_header[2]
            else:
                self.headers[parsed_header[0]] = parsed_header[1]

        return self

    def _parse_kafka_msg_second_part(self, kafka_raw_msg_second):
        parsed_body = kafka_raw_msg_second.split("\n")
        if not parsed_body[0][0] == "2":
            self.body = parsed_body[0]

        return self

    def _parse_kafka_msg_third_part(self, kafka_raw_msg_third):
        parsed_response = kafka_raw_msg_third.split("\n")
        self.response_body = parsed_response[1]
        return self

    def parse_kafka_msg(self, msg):
        parsed_result = msg.split("\n\n")
        self._parse_kafka_first_header(parsed_result[0])
        self._parse_kafka_msg_second_part(parsed_result[1])
        self._parse_kafka_msg_third_part(parsed_result[2])


def parse_msg():
    with open('http_traffic', 'r') as f:
        result = f.read()
        http_traffic = HttpTraffic()
        http_traffic.parse_kafka_msg(result)
        print(http_traffic)


parse_msg()
