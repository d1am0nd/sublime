import sublime
import sublime_plugin
import re

class PhpTestInitiateCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            line = self.view.line(region)
            content = self.view.substr(line)

            m = re.search('^\s+', content)
            if m is None:
                start_spaces = ""
            else:
                start_spaces = m.group(0)

            underscored = self.view.substr(line).strip().replace(" ", "_")
            content = start_spaces + "/** @test */ \n" + start_spaces + "function " + underscored + "()"
            self.view.replace(edit, line, content)
