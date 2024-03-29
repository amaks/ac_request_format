import sublime, sublime_plugin

class AcRequestFormatCommand(sublime_plugin.TextCommand):
  def run(self, edit):

    region = self.view.sel()[0]
    if not region.empty():
      blocks             = self.view.substr(region).split('.')
      startrow, startcol = self.view.rowcol(region.begin())
      new_line           = ''
      first_line         = 0

      for block in blocks:
        if blocks.index(block) == 0:
          new_line  += block + '.'
          first_line = len(block) + startcol
        elif blocks.index(block) == 1:
          new_line  += block
        else:
          spaces    = [" " for x in range(first_line)]
          if 'joins' in block or 'where' in block or 'order' in block or 'limit' in block:
            new_line += '\n' + ''.join(spaces) + '.' + block
          else:
            new_line += '.' + block

      self.view.replace(edit, region, new_line)