__author__ = 'hanzhao'
# encoding : utf-8

import json
import os

def plugin_name():
        pluginname = []
        for filename in os.listdir("plugins"):
                if not filename.endswith(".py") or filename.startswith("_"):
                    continue
                else :
                    pluginname.append(filename[:-3])
        return pluginname
pluglist = plugin_name()

class PluginManager(object):



    def load_config(self, id):
        """
        You can load plugin config any time, then load plugin.
        :typ groupid: str or unicode
        """
        with open('config/plug_config.json',"r") as f:
            try:
                config = json.load(f)[id]['plugin_on']
            except:
                config = json.load(open('config/plug_config.json',"r"))['default']['plugin_on']
        return config

    # def save_config(self,id,config):
    #     with open('config/plug_config.json',"w") as f:
    #         raw_config = json.load(f)
    #         if id in raw_config:
    #             old_config = raw_config[id]
    #             new_config = old_config['plugin_on'].append(plugname)
    #             raw_config[id]['plugin_on'] = new_config
    #             f.write(json.dumps(raw_config))
    #         else:
    #             pass





    def open_plugin(self,id,plugname):
        if plugname in pluglist:
            with open('config/plug_config.json',"r") as f:
                raw_config = json.load(f)
                if id in raw_config:
                    old_config = raw_config[id]
                    old_config['plugin_on'].append(plugname)
                    raw_config[id]['plugin_on'] = old_config['plugin_on']
                    fp = open('config/plug_config.json',"w")
                    fp.write(json.dumps(raw_config))
                else:
                    old_config = {id:{"plugin_on":["base","rubik_tool","rubik_scramble"]}}
                    old_config[id]['plugin_on'].append(plugname)
                    raw_config[id] = old_config[id]
                    fp = open('config/plug_config.json',"w")
                    fp.write(json.dumps(raw_config))

    def close_plugin(self,id,plugname):
        if plugname in pluglist and plugname!='base':
            with open('config/plug_config.json',"r") as f:
                raw_config = json.load(f)
                if id in raw_config:
                    old_config = raw_config[id]
                    if plugname in old_config['plugin_on']:
                        plugarr = old_config['plugin_on']
                        plugarr.remove(plugname)
                        raw_config[id]['plugin_on'] = plugarr
                else:
                    if plugname in ["base","rubik_tool","rubik_scramble"]:
                        plugarr = ["base","rubik_tool","rubik_scramble"]
                        plugarr.remove(plugname)
                        new_config ={id:{"plugin_on":plugarr}}
                        raw_config[id] = new_config[id]
                fp = open('config/plug_config.json',"w")
                fp.write(json.dumps(raw_config))
#
# aa = PluginManager()
# aa.close_plugin('bbb','base')