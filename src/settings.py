#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

import random


class Settings:
    """
    Class for managing basic execution settings and information.
    """

    def __init__(self):

        self.__init_seed_list()

        # LOCAL SEARCH METHOD PARAMETERS
        self.LOCAL_SEARCH_NUM_ITERATIONS = 10000

        # SIMULATED ANNEALING PARAMETERS
        self.SA_FINAL_TEMPERATURE = 0.1

        self.SA_FIRST_PHASE_NUM_ITERATIONS = 100
        self.SA_FIRST_PHASE_ACCEPT_WORSE_PROB = 0.8

        self.SA_FINAL_PHASE_NUM_ITERATIONS = 9900


    def init_random_number_gen(self,
                               idx: int):
        """
        Initializes Python random number generator (in Module random) with one
        of the seeds stored in this class.

        Params:
        idx -- a number between 1 and 123, used to index the seed collection
        """
        assert(int(idx) > 0)

        if int(idx) <= len(self.random_seed_list):
            random.seed(self.random_seed_list[int(idx)-1])
        else:
            print("ERROR: random seed index is greater than the number of seeds stored")
            quit()


    def __init_seed_list(self):
        """
        Collection of 123 random primes with 10 digits obtained from:
        https://bigprimes.org/
        """
        self.random_seed_list = [
            2617219109,
            7432165739,
            1786517701,
            1867444063,
            4419385207,
            6247563979,
            7066208323,
            7303530133,
            5519238587,
            4587517367,
            3277147501,
            7838050093,
            1793352137,
            6981948469,
            7184188393,
            5912214703,
            9188059571,
            9517456967,
            9815513203,
            8293660747,
            9833414203,
            3787385977,
            2236317497,
            3394998913,
            3718979189,
            5209476197,
            4517421721,
            2045508077,
            4653768913,
            5646402499,
            9774302273,
            7910653831,
            7705344203,
            3637798369,
            8968264463,
            9923829947,
            9715677401,
            6231789791,
            4065809809,
            1030333847,
            3730183637,
            3409623869,
            9913458461,
            3972809801,
            9710344541,
            2730423401,
            5926242941,
            9378711053,
            7650435643,
            8030269759,
            5136169237,
            2259079129,
            3463385969,
            5181178907,
            2984265259,
            4891207289,
            7525629029,
            3018384637,
            2501868307,
            8125284779,
            4777326403,
            1793231789,
            1145951467,
            5846814277,
            5805611869,
            4977367207,
            7228350487,
            5715411001,
            9876899693,
            6584495549,
            8631490957,
            4532074243,
            3258972523,
            4647722047,
            9775905941,
            4932341341,
            8720770501,
            2920092449,
            7136358013,
            4016048893,
            1159773491,
            1953158957,
            5490631577,
            1328527429,
            9965585527,
            3466521103,
            8784060697,
            6678064109,
            3953463659,
            1593742187,
            2011811299,
            3358663621,
            2577264259,
            8477535137,
            7027551257,
            3653105153,
            2387579797,
            8112397039,
            3002731343,
            1574022563,
            3441169307,
            5643690421,
            8395682857,
            4349701831,
            1906797437,
            4671256459,
            4149188789,
            7692870293,
            1954144757,
            5574989419,
            3124509529,
            3944975173,
            9986299859,
            6790299037,
            5204026813,
            8362564831,
            6505328147,
            7186549291,
            1164998981,
            4843925587,
            1164395993,
            9020528753,
            1585075753,
        ]
