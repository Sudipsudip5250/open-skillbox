---
name: user-threejs-3d-development
description: Build, debug, optimize, or improve Three.js and browser-based 3D experiences. Use for scenes, cameras, geometry, materials, lighting, shaders, GLTF/GLB assets, post-processing, interaction, WebGPU/WebGL, or 3D visual polish outside a complete game workflow.
---

# Three.js and Browser 3D

## Quick start

Use this skill when the request matches **Build, debug, optimize, or improve Three.js and browser-based 3D experiences. Use for scenes, cameras, geometry, materials, lighting, shaders, GLTF/GLB assets, post-processing, interaction, WebGPU/WebGL, or 3D visual polish outside a complete game workflow.** Start with the smallest defensible input set, state what is known and unknown, then follow the method-selection workflow. Produce an intermediate record before the final answer so another agent can review or continue the work.


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

## Inputs and decision points

| Stage | Required record | Decision or escalation |
|---|---|---|
| Frame | Request, audience, scope, constraints, permissions, source material, and expected precision | If a required input is missing, ask one blocking question or label the assumption. |
| Select | Applicable method, alternatives considered, and why the selected path fits | Inspect the repository, runtime, dependency versions, interfaces, configuration, and existing tests before choosing an implementation or diagnostic path. |
| Act | Ordered steps, tool or artifact inputs, expected intermediate result, and stop condition | Keep changes reversible and record approval before external, destructive, or high-impact actions. |
| Interpret | Result, uncertainty, limitations, and what would change the conclusion | Separate verified observations, calculations, inferences, and recommendations. |

## Worked pattern

For a request involving **threejs-3d-development**, use this compact record:

```text
Request: [the concrete task and intended outcome]
Scope and inputs: [files, data, versions, permissions, audience]
Classification: [task type, risk, and relevant branch]
Method: [selected procedure and why alternatives were rejected]
Steps: [ordered actions with intermediate outputs]
Result: [answer or artifact, separated from interpretation]
Checks: [independent verification, edge cases, safety, accessibility, or reproducibility]
Handoff: [files, owners, limitations, and next action]
```

Do not fill this pattern with invented evidence. If the task is underspecified, keep placeholders visible or ask for the missing decision.

## Failure handling

When the normal path fails, reduce the problem to the smallest reproducible case, preserve the original inputs, and record the first failing step. If the failure is not reproducible, capture environment and logs, reduce the case, state uncertainty, and avoid speculative rewrites or destructive recovery steps. If a tool, source, or host is unavailable, provide a tool-neutral alternative and label what remains unverified.

## Portability and maintenance

Keep the procedure independent of a particular agent host, shell, vendor, model, or private repository. Use canonical `SKILL.md` instructions and refer to host-specific setup only through documented adapters. For software and systems, record the relevant version, source date, configuration, or environment when it can change the result. Re-check this skill when an API, standard, policy, model capability, safety requirement, or user workflow changes.

## Verification and quality checks

run the narrowest relevant tests, type/build checks, runtime reproduction, compatibility checks, rollback review, and an inspection of the final diff for unintended behavior. Record the exact checks run, what they establish, what they cannot establish, and any manual or unavailable check.

## Handoff

Report the chosen renderer and version assumptions, assets and licenses, visual changes, performance measurements, tested interactions and viewports, fallback behavior, and known risks. For complete playable games, hand off to the existing game-development workflow.
