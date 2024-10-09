from algorithm_execution import algorithm_execution
import matplotlib.pyplot as plt


class AdditionOfNewGoalsPlot:
    def __init__(self, algorithm_execution):
        self.algorithm_execution = algorithm_execution

    def get_y_values(self):
        y_values_per_iteration = [0] * len(self.algorithm_execution.iterations)

        newly_created_goals = []
        for goal in self.algorithm_execution.goals:  # Fixed to use self.algorithm_execution
            if goal.not_among_goals_at_start:
                newly_created_goals.append(goal)

        for goal in newly_created_goals:
            y_values_per_iteration[goal.created_in_iteration_number] += 1
        
        for i in range(1, len(y_values_per_iteration)):
            y_values_per_iteration[i] += y_values_per_iteration[i - 1]

        return y_values_per_iteration
    
    def plot_number_of_goals_not_among_initial_goals(self, show=False):
        y_values = self.get_y_values()
        x_values = range(len(y_values))

        # Create a figure and axis
        fig, ax = plt.subplots()
        
        # Plot the data
        ax.plot(x_values, y_values)
        ax.set_xlabel('Iteration number')
        ax.set_ylabel('Number of goals not among the initial goals')
        #ax.set_title('Number of goals not among the initial goals per Iteration' + ' for ' + self.algorithm_execution.name)
        title = 'Number of goals that did not exist at the start' + ' for ' + self.algorithm_execution.name
        

        if show:
            plt.show()
        
        return fig