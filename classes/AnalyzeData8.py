import numpy as np

class AnalyzeData:
    def __init__(self, params={}):
        self.pi = np.pi
        self.d2r = self.pi/180
        # If file name is present, use the value, 
        # else, use a blank string
        self.fname = params.get("fname", "")

    def load_data(self, fname="", retvals=False):
        if self.fname and fname == "":
            fname = self.fname

        eeg = np.load(fname)
        print("Data Loaded ...")

        data = eeg["data"]
        sr = eeg["sr"]
        tx = eeg["tx"]
        cond_labels = eeg["cond_labels"]

        if retvals:
            return data, sr, tx, cond_labels
        else:
            self.data = data
            self.sr = sr
            self.tx = tx
            self.cond_labels = cond_labels

    def mean_rows(self, data=[], retvals=False):
        if data==[]:
            data = self.data
        val = np.mean(data, axis=0)
        if retvals:
            return val
        else:
            self.mr_data = val

    def mean_cols(self, data=[], retvals=False):
        if data==[]:
            data = self.data
        val = np.mean(data, axis=1)
        if retvals:
            return val
        else:
            self.mc_data = val

    def get_deg_rads(self, angs, steps):
        d = np.linspace(angs[0], angs[1], steps)
        r = self.d2r * d
        return r