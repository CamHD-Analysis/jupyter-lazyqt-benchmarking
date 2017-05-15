import pycamhd.native as native

class PycamhdAccessor:
    def __init__(self, base_dir ):
        self.base_dir = base_dir

    def merge_url( self, path ):
        return self.base_dir + path

    def get_metadata( self, url ):
        return pycamhd.movie_info( self.merge_url( url ) )

    def get_frame( self, url, frame_num, format = 'np'):
        return native.get_frame(self.merge_url( url ), frame_num, 'rgb24')