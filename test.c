#include <SDL2/SDL.h>
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <time.h>

#define SCREEN_WIDTH 640
#define SCREEN_HEIGHT 480
#define CELL_SIZE 20
#define MAZE_WIDTH (SCREEN_WIDTH / CELL_SIZE)
#define MAZE_HEIGHT (SCREEN_HEIGHT / CELL_SIZE)

SDL_Window *window = NULL;
SDL_Renderer *renderer = NULL;

typedef struct {
    int x, y;
} Point;

enum {
    WALL = 0,
    PATH = 1
};

int maze[MAZE_HEIGHT][MAZE_WIDTH];

void generateMaze(Point p) {
    maze[p.y][p.x] = PATH;
    int dirs[4][2] = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
    for (int i = 0; i < 4; ++i) {
        int r = rand() % 4;
        int temp = dirs[i][0];
        dirs[i][0] = dirs[r][0];
        dirs[r][0] = temp;
        temp = dirs[i][1];
        dirs[i][1] = dirs[r][1];
        dirs[r][1] = temp;
    }
    for (int i = 0; i < 4; ++i) {
        int nx = p.x + dirs[i][0] * 2;
        int ny = p.y + dirs[i][1] * 2;
        if (nx >= 0 && nx < MAZE_WIDTH && ny >= 0 && ny < MAZE_HEIGHT && maze[ny][nx] == WALL) {
            maze[p.y + dirs[i][1]][p.x + dirs[i][0]] = PATH;
            generateMaze((Point){nx, ny});
        }
    }
}

void drawMaze() {
    SDL_SetRenderDrawColor(renderer, 255, 255, 255, SDL_ALPHA_OPAQUE);
    SDL_RenderClear(renderer);
    SDL_SetRenderDrawColor(renderer, 0, 0, 0, SDL_ALPHA_OPAQUE);
    for (int y = 0; y < MAZE_HEIGHT; ++y) {
        for (int x = 0; x < MAZE_WIDTH; ++x) {
            if (maze[y][x] == WALL) {
                SDL_Rect wallRect = {x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE};
                SDL_RenderFillRect(renderer, &wallRect);
            }
        }
    }
    SDL_RenderPresent(renderer);
}

void cleanup() {
    if (renderer) {
        SDL_DestroyRenderer(renderer);
        renderer = NULL;
    }
    if (window) {
        SDL_DestroyWindow(window);
        window = NULL;
    }
    SDL_Quit();
}

int main(int argc, char *argv[]) {
    if (SDL_Init(SDL_INIT_VIDEO) != 0) {
        printf("SDL_Init error: %s\n", SDL_GetError());
        return 1;
    }
    srand(time(NULL));

    window = SDL_CreateWindow("Maze Generator", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, SCREEN_WIDTH, SCREEN_HEIGHT, SDL_WINDOW_SHOWN);
    if (!window) {
        printf("SDL_CreateWindow error: %s\n", SDL_GetError());
        cleanup();
        return 1;
    }

    renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED | SDL_RENDERER_PRESENTVSYNC);
    if (!renderer) {
        printf("SDL_CreateRenderer error: %s\n", SDL_GetError());
        cleanup();
        return 1;
    }

    Point start = {1, 1};
    for (int y = 0; y < MAZE_HEIGHT; ++y) {
        for (int x = 0; x < MAZE_WIDTH; ++x) {
            maze[y][x] = WALL;
        }
    }

    generateMaze(start);
    drawMaze();

    SDL_Event event;
    bool quit = false;
    while (!quit) {
        while (SDL_PollEvent(&event)) {
            if (event.type == SDL_QUIT) {
                quit = true;
            }
        }
    }

    cleanup();
    return 0;
}
