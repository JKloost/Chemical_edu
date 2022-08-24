from unittest import TestCase
from main_code import statistics as st, database_reader as data


class TestStatistics(TestCase):
    def setUp(self):
        self.statistics = st.Statistics()

    def test_statistics_window(self):
        # Remember actual scores
        path = data.get_path()
        statistics_file_realscore = open(path + '/statistics.txt', 'r').read().splitlines()

        # Test writing the file for asserts
        statistics_file = open(path + '/statistics.txt', 'w')
        statistics_file.write('25 Oct 2018 09:07:32 50\n24 Oct 2018 10:05:20 20\n')
        statistics_file.close()

        # Run update to test
        st.update(10, "24 Oct 2018 10:15:20")

        # Run tests 1
        self.statistics.statistics_window()
        assert st.number10['text'] == '10.'
        assert st.score1['text'] == '50'
        assert st.record1['text'] == '25 Oct 2018 09:07:32'
        assert st.score2['text'] == "20"
        assert st.record2['text'] == "24 Oct 2018 10:05:20"

        # Test if score was written to file with update method
        assert st.score3['text'] == "10"
        assert st.record3['text'] == "24 Oct 2018 10:15:20"

        # Test update replace method and auto sort system
        statistics_file = open(path + '/statistics.txt', 'w')
        statistics_file.write('25 Oct 2018 09:07:32 10\n24 Oct 2018 10:05:20 9\n''25 Oct 2018 09:07:32 8\n24 Oct 2018'
                              ' 10:05:20 7\n''25 Oct 2018 09:07:32 6\n24 Oct 2018 10:05:20 5\n''25 Oct 2018 09:07:32'
                              ' 4\n24 Oct 2018 10:05:20 3\n25 Oct 2018 09:07:32 2\n24 Oct 2018 10:05:20 1\n')
        statistics_file.close()

        # Replace last record with score of 1 and check that lowest score is now indeed 2 instead of 1
        st.update(200, "31 dec 1999 23:59:59")
        self.statistics.statistics_window()
        assert st.score1['text'] == '200'
        assert st.score10['text'] == '2'

        # Restore actual scores
        statistics_file = open(path + '/statistics.txt', 'w')
        for line in statistics_file_realscore:
            statistics_file.write(line + '\n')