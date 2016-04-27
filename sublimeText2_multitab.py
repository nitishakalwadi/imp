import sublime, sublime_plugin

multi_col_layout = 1

class MultiColumnTabBarCommand(sublime_plugin.EventListener):
  def on_activated(self,view):
    a=sublime.active_window()
    b=a.get_view_index(view)
    if (b[0] == 0) and (multi_col_layout == 1):
      a.run_command("set_layout",{"cols": [0.0 ,1],"rows": [0.0, 0.05, 0.1, 1.0],"cells": [[0, 2, 1, 3],[0, 0, 1, 1],[0, 1, 1, 2]]})
    
    if b[0] == 1 and (multi_col_layout == 1):
      a.run_command("set_layout",{"cols": [0.0 ,1],"rows": [0.0, 0.05, 0.1, 1.0],"cells": [[0, 0, 1, 1],[0, 2, 1, 3],[0, 1, 1, 2]]})
    
    if b[0] == 2 and (multi_col_layout == 1):
      a.run_command("set_layout",{"cols": [0.0 ,1],"rows": [0.0, 0.05, 0.1, 1.0],"cells": [[0, 0, 1, 1],[0, 1, 1, 2], [0, 2, 1, 3]]})
            
class ToggleMultiColLayoutCommand(sublime_plugin.TextCommand):
  def run(self,edit):
    global multi_col_layout    
    if (multi_col_layout == 1):
      multi_col_layout = 0
      print "Multi Column switch disabled"
    elif (multi_col_layout == 0):
      multi_col_layout = 1
      print "Multi Column switch enabled"
      
class DisableMultiColLayoutCommand(sublime_plugin.TextCommand):
  def run(self,edit):
    global multi_col_layout
    multi_col_layout = 0
    print "Multi Column switch disabled"

class EnableMultiColLayoutCommand(sublime_plugin.TextCommand):
  def run(self,edit):
    global multi_col_layout
    multi_col_layout = 1
    print "Multi Column switch enabled"
