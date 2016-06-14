import sublime, sublime_plugin, os

class goinstall(sublime_plugin.EventListener):
	
	def on_post_save(self, view):
		if view.file_name().endswith('.go') is not True:
			return

		folder = os.path.dirname(view.file_name())
		view.window().run_command('exec',{'cmd':['/bin/go',"install"],'working_dir':folder})
