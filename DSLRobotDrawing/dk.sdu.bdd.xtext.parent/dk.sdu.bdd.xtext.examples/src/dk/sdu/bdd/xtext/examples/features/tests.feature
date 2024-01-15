
	
			 

Feature: Robot drawing a square

	Scenario: Given the beautifulFigure "SuperSquare" is NOT DONE
        Given the beautifulFigure "SuperSquare" is NOT DONE
        And the robot "SuperRobot" moves to position "upper right" with "very slow" speed
        When the position of the robot "SuperRobot" is "upper right"
        And the robot "SuperRobot" moves to position "lower right" with "fast" speed
        Then the position of the robot "SuperRobot" is "lower right"

	Scenario: When the beautifulFigure "SuperSquare" is ALMOST DONE
        Given the beautifulFigure "SuperSquare" is ALMOST DONE
        When the robot "SuperRobot" moves to position "lower left" with "very fast" speed
        Then the position of the robot "SuperRobot" is "lower left"

	Scenario: Then the robot "SuperRobot" moves to position "upper left" with "very slow" speed
        Given the robot "SuperRobot" moves to position "upper left" with "very slow" speed
        And the position of the robot "SuperRobot" is "upper left"
        When the position of the robot "SuperRobot" is "upper left"
        Then the beautifulFigure "SuperSquare" is DONE
