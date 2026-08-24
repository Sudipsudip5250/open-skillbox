---
name: user-media-provenance-privacy
description: Inspect, preserve, validate, or selectively remove metadata from authorized images, audio, video, documents, and generated media. Use for EXIF/GPS privacy, IPTC/XMP, C2PA content credentials, provenance, media authenticity, publication hygiene, or metadata-leak review.
---

# Media Provenance and Privacy

## Workflow

1. Confirm ownership or permission, source and derivative files, intended publication channel, privacy objective, required attribution, provenance needs, and whether the task is analysis, preservation, or cleanup.
2. Inventory metadata and embedded content: EXIF, GPS, timestamps, device identifiers, IPTC, XMP, ICC profiles, thumbnails, audio/video tags, document properties, C2PA manifests, filenames, paths, and file-system metadata.
3. Classify each field as required for rendering, accessibility, attribution, licensing, provenance, workflow, or unnecessary personal or operational data. Preserve a private original and record hashes or version identifiers.
4. Apply the smallest authorized change. Remove only unnecessary privacy-sensitive fields; preserve color profiles, captions, licensing, accessibility, provenance, and required technical metadata. If content credentials are present, explain the effect before changing them.
5. Validate the output by re-reading metadata, checking hashes and rendering, testing the target platform, and confirming that the requested privacy goal was met without claiming that every trace has disappeared.
6. Maintain a change record with source, tool and version, fields changed, output hash, reviewer, license, and publication decision.

## Rules

- This skill supports privacy protection and authorized cleanup only. It must not be used to evade attribution, copyright enforcement, platform safeguards, forensic review, moderation, or lawful investigation.
- Do not remove C2PA or provenance records merely to make content harder to detect or misattribute. Explain trade-offs and preserve the original.
- Do not claim that metadata removal erases all identifying traces; file content, visual fingerprints, server logs, upload records, and platform records may remain.
- Do not delete GPS, creator, license, or accessibility information when the project requires it or the user has not authorized removal.
- Do not process third-party media without confirmed rights and a legitimate privacy or publication purpose.

## Handoff

Report authorization, original preservation, metadata inventory, fields changed or retained, provenance impact, validation results, residual traces, hashes, tool versions, and publication risks.
