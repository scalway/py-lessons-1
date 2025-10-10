"""
AI Agent Examples - Basic Agent Architectures

This module demonstrates basic AI agent concepts and patterns.
These are educational examples showing agent design principles.
"""

import random
from abc import ABC, abstractmethod
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass
from enum import Enum


class Action(Enum):
    """Available actions for agents."""
    MOVE_UP = "up"
    MOVE_DOWN = "down"
    MOVE_LEFT = "left"
    MOVE_RIGHT = "right"
    STAY = "stay"
    PICK_UP = "pick_up"
    DROP = "drop"


@dataclass
class Percept:
    """Agent's perception of the environment."""
    location: Tuple[int, int]
    nearby_objects: List[str]
    battery_level: int
    is_goal_reached: bool


def simple_reflex_agent_example():
    """Demonstrate a simple reflex agent."""
    print("=" * 50)
    print("SIMPLE REFLEX AGENT")
    print("=" * 50)
    
    class VacuumCleanerAgent:
        """Simple vacuum cleaner that reacts to dirt."""
        
        def __init__(self):
            self.location = 'A'
        
        def perceive(self, environment):
            """Perceive the current location's state."""
            return environment.get(self.location, 'clean')
        
        def decide_action(self, percept):
            """Decide action based on current percept only."""
            if percept == 'dirty':
                return 'clean'
            elif self.location == 'A':
                return 'move_right'
            elif self.location == 'B':
                return 'move_left'
            return 'stay'
        
        def act(self, action, environment):
            """Execute the action."""
            if action == 'clean':
                environment[self.location] = 'clean'
                print(f"  Cleaning location {self.location}")
            elif action == 'move_right':
                self.location = 'B'
                print(f"  Moving to location B")
            elif action == 'move_left':
                self.location = 'A'
                print(f"  Moving to location A")
    
    # Simulate environment
    environment = {'A': 'dirty', 'B': 'dirty'}
    agent = VacuumCleanerAgent()
    
    print(f"Initial environment: {environment}")
    print("\nAgent actions:")
    
    for step in range(5):
        percept = agent.perceive(environment)
        action = agent.decide_action(percept)
        agent.act(action, environment)
    
    print(f"\nFinal environment: {environment}")


def model_based_agent_example():
    """Demonstrate a model-based agent."""
    print("\n" + "=" * 50)
    print("MODEL-BASED AGENT")
    print("=" * 50)
    
    class RobotAgent:
        """Robot with internal model of the world."""
        
        def __init__(self, grid_size: int = 5):
            self.grid_size = grid_size
            self.position = (0, 0)
            self.visited = set()
            self.world_model = {}  # Internal representation
            self.energy = 100
        
        def perceive(self, environment):
            """Perceive surroundings and update world model."""
            x, y = self.position
            self.world_model[self.position] = environment.get(self.position, 'empty')
            self.visited.add(self.position)
            return self.world_model[self.position]
        
        def decide_action(self):
            """Decide based on internal model."""
            if self.energy < 20:
                return Action.STAY  # Conserve energy
            
            x, y = self.position
            possible_moves = [
                (x, y + 1, Action.MOVE_UP),
                (x, y - 1, Action.MOVE_DOWN),
                (x + 1, y, Action.MOVE_RIGHT),
                (x - 1, y, Action.MOVE_LEFT),
            ]
            
            # Prefer unvisited locations
            unvisited = [
                (nx, ny, action) for nx, ny, action in possible_moves
                if 0 <= nx < self.grid_size and 0 <= ny < self.grid_size
                and (nx, ny) not in self.visited
            ]
            
            if unvisited:
                _, _, action = random.choice(unvisited)
                return action
            
            return Action.STAY
        
        def act(self, action: Action):
            """Execute action and update state."""
            x, y = self.position
            
            if action == Action.MOVE_UP:
                self.position = (x, min(y + 1, self.grid_size - 1))
            elif action == Action.MOVE_DOWN:
                self.position = (x, max(y - 1, 0))
            elif action == Action.MOVE_RIGHT:
                self.position = (min(x + 1, self.grid_size - 1), y)
            elif action == Action.MOVE_LEFT:
                self.position = (max(x - 1, 0), y)
            
            self.energy -= 5
            print(f"  Position: {self.position}, Energy: {self.energy}, " +
                  f"Visited: {len(self.visited)} locations")
    
    environment = {(2, 2): 'obstacle', (3, 3): 'goal'}
    agent = RobotAgent()
    
    print("Robot exploring environment...")
    for step in range(10):
        agent.perceive(environment)
        action = agent.decide_action()
        agent.act(action)
    
    print(f"\nExplored {len(agent.visited)} locations")


def goal_based_agent_example():
    """Demonstrate a goal-based agent."""
    print("\n" + "=" * 50)
    print("GOAL-BASED AGENT")
    print("=" * 50)
    
    class PathFinderAgent:
        """Agent that finds path to goal."""
        
        def __init__(self, start: Tuple[int, int], goal: Tuple[int, int]):
            self.position = start
            self.goal = goal
            self.path = []
        
        def find_path(self):
            """Simple path planning using Manhattan distance."""
            current = self.position
            path = [current]
            
            while current != self.goal:
                x, y = current
                gx, gy = self.goal
                
                # Move towards goal
                if x < gx:
                    current = (x + 1, y)
                elif x > gx:
                    current = (x - 1, y)
                elif y < gy:
                    current = (x, y + 1)
                elif y > gy:
                    current = (x, y - 1)
                
                path.append(current)
            
            return path
        
        def execute(self):
            """Execute the planned path."""
            self.path = self.find_path()
            print(f"  Start: {self.position}")
            print(f"  Goal: {self.goal}")
            print(f"  Path: {' -> '.join(str(p) for p in self.path)}")
            print(f"  Steps: {len(self.path) - 1}")
    
    agent = PathFinderAgent(start=(0, 0), goal=(5, 3))
    agent.execute()


def utility_based_agent_example():
    """Demonstrate a utility-based agent."""
    print("\n" + "=" * 50)
    print("UTILITY-BASED AGENT")
    print("=" * 50)
    
    class ResourceGatherer:
        """Agent that maximizes resource collection utility."""
        
        def __init__(self):
            self.position = (0, 0)
            self.resources = 0
            self.energy = 100
        
        def calculate_utility(self, action_result: Dict) -> float:
            """Calculate utility of an action result."""
            resource_value = action_result.get('resources', 0) * 10
            energy_cost = action_result.get('energy_cost', 0) * -1
            distance = action_result.get('distance', 0) * -0.5
            
            return resource_value + energy_cost + distance
        
        def evaluate_options(self, options: List[Dict]) -> Dict:
            """Choose action with highest utility."""
            best_option = max(options, key=lambda x: self.calculate_utility(x))
            return best_option
        
        def decide(self):
            """Decide action based on utility."""
            options = [
                {
                    'action': 'gather_nearby',
                    'resources': 5,
                    'energy_cost': 10,
                    'distance': 1
                },
                {
                    'action': 'move_to_rich_area',
                    'resources': 15,
                    'energy_cost': 30,
                    'distance': 5
                },
                {
                    'action': 'return_to_base',
                    'resources': 0,
                    'energy_cost': 20,
                    'distance': 3
                }
            ]
            
            best = self.evaluate_options(options)
            utility = self.calculate_utility(best)
            
            print(f"  Current state: Resources={self.resources}, Energy={self.energy}")
            print(f"  Evaluating options:")
            for opt in options:
                print(f"    {opt['action']}: utility = {self.calculate_utility(opt):.1f}")
            print(f"  Chosen action: {best['action']} (utility: {utility:.1f})")
    
    agent = ResourceGatherer()
    agent.decide()


def multi_agent_system_example():
    """Demonstrate simple multi-agent interaction."""
    print("\n" + "=" * 50)
    print("MULTI-AGENT SYSTEM")
    print("=" * 50)
    
    class WorkerAgent:
        """Simple worker agent."""
        
        def __init__(self, agent_id: int, skill: str):
            self.id = agent_id
            self.skill = skill
            self.tasks_completed = 0
        
        def can_do_task(self, task: str) -> bool:
            """Check if agent can perform task."""
            return task == self.skill
        
        def do_task(self, task: str):
            """Perform task if capable."""
            if self.can_do_task(task):
                self.tasks_completed += 1
                return True
            return False
    
    class CoordinatorAgent:
        """Coordinator for worker agents."""
        
        def __init__(self):
            self.workers: List[WorkerAgent] = []
            self.task_queue: List[str] = []
        
        def add_worker(self, worker: WorkerAgent):
            """Add worker to the system."""
            self.workers.append(worker)
        
        def add_task(self, task: str):
            """Add task to queue."""
            self.task_queue.append(task)
        
        def assign_tasks(self):
            """Assign tasks to capable workers."""
            print("  Assigning tasks...")
            for task in self.task_queue[:]:
                for worker in self.workers:
                    if worker.can_do_task(task):
                        if worker.do_task(task):
                            print(f"    Worker {worker.id} ({worker.skill}) completed: {task}")
                            self.task_queue.remove(task)
                            break
                else:
                    print(f"    No worker available for: {task}")
    
    # Create multi-agent system
    coordinator = CoordinatorAgent()
    
    coordinator.add_worker(WorkerAgent(1, "coding"))
    coordinator.add_worker(WorkerAgent(2, "testing"))
    coordinator.add_worker(WorkerAgent(3, "coding"))
    
    coordinator.add_task("coding")
    coordinator.add_task("testing")
    coordinator.add_task("coding")
    coordinator.add_task("design")
    
    coordinator.assign_tasks()
    
    print("\n  Summary:")
    for worker in coordinator.workers:
        print(f"    Worker {worker.id} ({worker.skill}): {worker.tasks_completed} tasks")


if __name__ == "__main__":
    simple_reflex_agent_example()
    model_based_agent_example()
    goal_based_agent_example()
    utility_based_agent_example()
    multi_agent_system_example()
    print("\n" + "=" * 50)
    print("All examples completed!")
    print("=" * 50)
