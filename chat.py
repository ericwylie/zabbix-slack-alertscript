from httplib2 import Http
from json import dumps

#
# Get Subject and Message information from Zabbix
#
subject="$2"
body="$3"
message= subject + " " + body

#
# Send non-urgent Zabbix alerts to Hangouts Chat #OfficeTech Alerts
#
def main():
    url = 'https://chat.googleapis.com/v1/spaces/AAAAb9SjVtg/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=DchsM9XHz9BAXBp1sjFhyh_7xBOhHQ34SpDs6zUDCNE%3D'
    bot_message = {
        "cards": [
        {
            "header": {
                "title":"Zabbix Warning Received",
                "imageUrl":"https://assets.zabbix.com/img/newsletter/2016/icons/share-logo-z.png"
            },
            "sections": [
            {
                "widgets": [
                    {
                        "keyValue": {
                            "topLabel": "Subject",
                            "content": subject
                        }
                    },
                    {
                        "keyValue": {
                            "topLabel": "Message",
                            "content": message
                        }
                    },
                    {
                        "buttons": [
                            {
                                "textButton": {
                                    "text": "VIEW DASHBOARD",
                                    "onClick": {
                                        "openLink": {
                                            "url": "http://zabbix.in.customink.com/zabbix/zabbix.php?action=dashboard.view"
                                        }
                                    }
                                }
                            }]
                    }
                ]
            }]
        }]
    }

    #                         #"iconUrl": "https://assets.zabbix.com/img/newsletter/2016/icons/share-logo-z.png",
    #                         "button": {
    #                             "textButton": {
    #                                 "text": "View Dashboard",
    #                                 "onClick": {
    #                                     "openLink": {
    #                                         "url": "http://zabbix.in.customink.com/zabbix/zabbix.php?action=dashboard.view"
    #                                     }
    #                                 }
    #                             }
    #                         }
    #                 }
    #             }]
    #         }]
    #     }]
    # }

    
    message_headers = { 'Content-Type': 'application/json; charset=UTF-8'}

    http_obj = Http()

    response = http_obj.request(
        uri=url,
        method='POST',
        headers=message_headers,
        body=dumps(bot_message),
    )

    print(response)

if __name__ == '__main__':
    main()