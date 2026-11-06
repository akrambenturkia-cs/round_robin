# System Architecture

## Overview

The project simulates a load balancer using
the Round Robin scheduling algorithm.

## Components

### 1. Simulator
Generates incoming client requests.

### 2. Request
Represents an incoming request.

### 3. Load Balancer
Selects the next available backend server.

### 4. Server
Represents a backend server and processes requests.

### 5. Statistics
Collects and displays request distribution.

## Data Flow

Client
  |
  v
Simulator
  |
  v
Request Generator
  |
  v
Load Balancer
  |
  v
Backend Server
  |
  v
Statistics
  |
  v
Terminal Output

## Communication

The simulator creates requests and passes them
to the load balancer.

The load balancer selects an available server.

The server processes the request.

Statistics records the distribution.