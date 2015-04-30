import sublime, sublime_plugin

class MoveToOtherViewCommand(sublime_plugin.WindowCommand):
	def run(self):
		w = self.window
		view = w.active_view()
		location = w.get_view_index(view)

		if location[0] == 0:
			# split to two groups if needed
			if w.num_groups() == 1:
				w.set_layout({"cols": [0.0, 0.5, 1.0], "rows": [0.0, 1.0], "cells": [[0, 0, 1, 1], [1, 0, 2, 1]] })

			# move to the second group
			w.set_view_index(view, 1, 0);
		else:
			# move to the first group
			w.set_view_index(view, 0, 0);

		# if the previous group is now empty, collapse down to one
		if len(w.views_in_group(0)) < 1 or len(w.views_in_group(1)) < 1:
			# move all views into the first group
			for v in w.views():
				w.set_view_index(v, 0, 0);

			# collapse to a single group
			w.set_layout({"cols": [0.0, 1.0], "rows": [0.0, 1.0], "cells": [[0, 0, 1, 1]] })

		# todo: keep tabs alphabetized?

# Move cursor to top of visible area
class Move_caret_topCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		screenful = self.view.visible_region()

		col = self.view.rowcol(self.view.sel()[0].begin())[1]
		row = self.view.rowcol(screenful.a)[0]
		target = self.view.text_point(row, col)

		self.view.sel().clear()
		self.view.sel().add(sublime.Region(target))

# Move cursor to bottom of visible area
class Move_caret_bottomCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		screenful = self.view.visible_region()

		col = self.view.rowcol(self.view.sel()[0].begin())[1]
		row = self.view.rowcol(screenful.b)[0]
		target = self.view.text_point(row, col)

		self.view.sel().clear()
		self.view.sel().add(sublime.Region(target))
