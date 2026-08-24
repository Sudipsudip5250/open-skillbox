---
name: user-threejs-3d-development
description: Build, debug, optimize, or improve Three.js and browser-based 3D experiences. Use for scenes, cameras, geometry, materials, lighting, shaders, GLTF/GLB assets, post-processing, interaction, WebGPU/WebGL, or 3D visual polish outside a complete game workflow.
---

# Three.js and Browser 3D

## Workflow

1. Inspect the project’s Three.js version, renderer, asset pipeline, coordinate conventions, build tool, and current runtime errors.
2. Define the visual and interaction target, camera model, scene graph, asset budget, device targets, and required fallback behavior before implementation.
3. Use focused modules for scene setup, geometry, materials, lighting, loaders, animation, interaction, and post-processing. Keep render-loop responsibilities explicit.
4. Load assets asynchronously with visible loading and failure states. Prefer GLTF/GLB, compressed textures, caching, disposal, and stable paths. Never embed secrets or depend on unavailable external generation APIs without a fallback.
5. Design for performance: reuse geometry and materials, instance repeated objects, cap pixel ratio, avoid unnecessary per-frame allocations, dispose removed resources, and measure draw calls, triangles, textures, memory, and frame time.
6. Test resize, touch, keyboard, camera controls, object picking, loading failure, mobile viewport, reduced motion, and a non-blank render.
7. Verify with a production build, browser console check, screenshots or canvas inspection, and a performance snapshot when graphics or shaders change.

## Technical rules

- Use the project’s installed Three.js APIs and verify version-sensitive APIs against current official documentation.
- Keep world units, camera near/far planes, color management, tone mapping, shadows, and lighting intentional and documented.
- Prefer stable animation timing and delta clamping; do not let a stalled tab create a huge simulation step.
- Use raycasting and pointer normalization correctly; make interactive objects keyboard or UI accessible when the experience requires it.
- Treat models, textures, shaders, and remote URLs as untrusted inputs. Validate formats and avoid arbitrary code execution.
- Do not claim photorealistic, AAA, or production-ready quality from a static screenshot alone; require an active runtime and measured evidence.

## Handoff

Report the chosen renderer and version assumptions, assets and licenses, visual changes, performance measurements, tested interactions and viewports, fallback behavior, and known risks. For complete playable games, hand off to the existing game-development workflow.
