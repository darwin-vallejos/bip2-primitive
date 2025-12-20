\# BIP-2 Primitive Architecture



\## Architectural Boundary



The BIP-2 primitive is a pure computation unit.



It executes deterministic transforms but does not interpret,

validate, store, contextualize, or assign meaning to its output.



---



\## Responsibility



The primitive is responsible ONLY for:



\- Deterministic normalization

\- Canonicalization

\- Cryptographic hashing



---



\## Explicit Exclusions



The primitive MUST NEVER:

\- Perform validation

\- Handle identity

\- Attach timestamps

\- Maintain state

\- Perform networking

\- Coordinate parties

\- Act as a platform or service



---



\## Platform Separation Rule



Any system using this primitive MUST treat it as a black box.



The primitive is unaware of platforms.

Platforms must not alter the primitive.



---



\## Architectural Finality



This boundary is permanent.



Any violation of this boundary constitutes a new system,

not an extension of BIP-2.



