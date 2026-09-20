# Master requirements

This register was imported from URC_2027_Lean_Master.xlsx (updated September 15, 2026). The workbook labels all entries as **proposed** and uses 2026 references only. Confirm every competition-derived item against the current 2027 rulebook before approving a design.

Each entry is a team requirement rather than a replacement for the rulebook. Source / basis preserves the workbook's basis label and prior-master traceability. Status combines the workbook status and delivery stage.

## Requirement format

| ID | Requirement | Source / basis | Verification | Status |
| --- | --- | --- | --- | --- |
| REQ-XXX-001 | _Write a testable shall statement._ | Rulebook section X.Y or documented team basis | Inspection, analysis, test, or demonstration | Draft - Build first |

## Whole rover

| ID | Requirement | Source / basis | Verification | Status |
| --- | --- | --- | --- | --- |
| R01 | The complete rover shall fit inside a 1.2 m cube at weigh-in without disassembly. Folding and reorientation are allowed. | 2026 reference; prior IDs: GEN-001 | Measure the complete weigh-in configuration, including antennas and protrusions. | To do - Build first |
| R02 | Each deployed mission configuration shall weigh no more than 50 kg. | 2026 reference; prior IDs: GEN-002, MBP-005 | Weigh the rover with its battery, payload module and carried equipment. | To do - Build first |
| R03 | All distinct fielded rover parts across missions shall total no more than 70 kg. | 2026 reference; prior IDs: GEN-003, NEW-004 | Use one parts list; count shared parts once and apply the rule exclusions for spares and tools. | To do - Build first |
| R04 | The rover shall operate without a power or communications tether to C2 and without using ambient air for an energy-yielding chemical reaction. | 2026 reference; prior IDs: GEN-005, GEN-006 | Demonstrate untethered battery operation; inspect the selected power system. Rover-to-deployable tethers have separate rules. | To do - Build first |
| R05 | A visible, accessible red exterior pushbutton shall immediately stop rover motion and cut all battery power to every rover system. | 2026 reference; prior IDs: GEN-007 | Press the button while driving and operating the arm; verify every battery-fed system loses power. | To do - Build first |
| R06 | Following power loss, the rover shall remain within the tested safe motion envelope and shall not restart motion until a person deliberately rearms it. | Team safety choice; prior IDs: NEW-003 | Test with the arm loaded and rover on the chosen slope; check rolling, arm descent and object release, then restore power. | To do - Build first |
| R07 | Battery feeds and powered branches shall have protection matched to the wire, connector and load ratings. | Team safety choice; prior IDs: NEW-001 | Check the wiring diagram and installed protection against component ratings before powered testing. | To do - Build first |
| R08 | The electrical system shall operate the chosen simultaneous drive, arm and compute loads without exceeding equipment ratings or causing resets. | Team build choice; prior IDs: NEW-002 | Log supply voltage and current during a loaded drive and arm test. | To do - Build first |
| R09 | The rover shall perform its selected tasks at ambient temperatures up to 37.8 degrees C and with protection for field dust and light rain. | 2026 reference; prior IDs: GEN-008, MBP-003, MBP-004 | Inspect covers and cable entries; run the loaded system in warm conditions and carry out a practical controlled dust and light-rain check. | To do - Build first |
| R10 | The rover shall complete the selected mission sequence on usable battery energy, with the team's chosen reserve and only permitted battery changes. | Team target within mission rules; prior IDs: GEN-011 | Run the longest planned duty cycle with the real payload; record run time and remaining energy. Include the servicing-to-autonomy sequence. | To do - Build first |

### Open choices and implementation notes

| Requirement | Open choice or note |
| --- | --- |
| R06 | Choose safe carry poses and acceptable movement in the first loaded test; keep people clear. |
| R09 | Agree a repeatable exposure and run duration; no certification or IP rating is proposed. |
| R10 | Choose duration and reserve after the first power measurements. A mid-mission battery change is an intervention under the 2026 rules. |

## Base and service

| ID | Requirement | Source / basis | Verification | Status |
| --- | --- | --- | --- | --- |
| R11 | The battery, fuses and likely failure connectors shall be accessible with the team's field tools without removing unrelated major assemblies. | Team build choice; prior IDs: GEN-009, GEN-010, MBP-009, NEW-010 | Demonstrate battery replacement and one representative repair with power isolated. | To do - Build first |
| R12 | The rover shall have lifting and restraint points suitable for its loaded transport and field recovery configuration. | Team safety choice; prior IDs: MBP-008, C2R-006 | Demonstrate handling with the actual crew and restraints, without lifting by fragile parts or entering moving mechanisms. | To do - Build first |
| R13 | The installed arm, science equipment, radios and batteries shall attach securely and connect using the agreed mounting dimensions, voltages, pinouts and data messages. | Team build choice; prior IDs: MBP-007, MBP-011, MBP-012, SYS-008, SOF-014 | Assemble the real modules and exercise their connections; keep one current sketch and connector list. | To do - Build first |
| R14 | The loaded rover shall drive, turn and stop on the team's selected sand, gravel, rock and slope test route without damage or an unrecoverable stuck condition. | Team target informed by mission terrain; prior IDs: MBP-001, MBP-010, DEL-012, DEL-016, DEL-017, DEL-018, DEL-019, DEL-021, GEN-004 | Drive the marked route in both directions and record completion, stops and recoveries. | To do - Build first |

### Open choices and implementation notes

| Requirement | Open choice or note |
| --- | --- |
| R14 | Choose a safe, representative route and obstacle limits after early driving tests; measure useful progress instead of requiring a >4 km/h top speed. |

## Communications and controls

| ID | Requirement | Source / basis | Verification | Status |
| --- | --- | --- | --- | --- |
| R15 | Students shall operate the rover from a blind C2 station using rover data and cameras, with no external internet or satellite internet dependency. | 2026 reference; prior IDs: COM-001, COM-003, COM-008, C2R-001, SOF-015 | Run the selected tasks with internet disconnected and direct rover views blocked; check offline software/maps and C2 compatibility with supplied 120 V, 60 Hz power. | To do - Build first |
| R16 | The rover shall provide usable commands, video and essential telemetry over the selected mission routes, including representative obstructed paths and distances up to 1 km. | Team target informed by 2026 conditions; prior IDs: COM-002, COM-004, COM-005, COM-018 | Use the actual C2 antenna and payload; drive, stop and manipulate over a surveyed range test and selected obstruction cases. | To do - Build first |
| R17 | During manual operation, the rover shall stop driving and enter the tested safe arm state when commands become stale or the link is lost. | Team safety choice; prior IDs: SOF-005, DEL-011 | Interrupt the link during a loaded manual test; check stopping, retention and deliberate recovery. Test the separately chosen autonomy link-loss response. | To do - Build first |
| R18 | C2 shall let students command driving and selected payloads, select permitted operating modes, and view the cameras, battery, position and link status needed for those tasks. Stale data shall be distinguishable. | Team build choice; prior IDs: COM-027, SOF-001, SOF-002, SOF-003, SOF-004, SOF-006, SOF-007, SOF-008, DEL-014, DEL-024, DEL-025 | Complete a blind practice task, exercise mode changes and disconnect one feed to confirm the operator can identify the loss. | To do - Build first |
| R19 | The installed radio system shall support the permitted band settings and antenna arrangement for the competition. | 2026 reference; prior IDs: COM-007, COM-009, COM-010, COM-011, COM-012, COM-013, COM-014, COM-015, COM-016, COM-017, COM-019, COM-026, C2R-003 | Use checklist T04 to inspect settings, cables and antenna placement before transmitting. | To do - Build first |

### Open choices and implementation notes

| Requirement | Open choice or note |
| --- | --- |
| R16 | Choose representative obstructions and service limits from field tests. This is not a guarantee through every hill or blockage. |
| R17 | Set the timeout from stopping-distance and link tests. Choose whether autonomy safely continues or stops on link loss; a universal radio-loss stop is not asserted as a URC rule. |

## Arm and carrying

| ID | Requirement | Source / basis | Verification | Status |
| --- | --- | --- | --- | --- |
| R20 | The arm shall lift a 5 kg test payload through the selected pickup and carry poses without exceeding component ratings. | Team design target based on mission payloads; prior IDs: ARM-016 | Use the real arm and mount; test the most demanding selected pose. Full extension at 5 kg is required only if a selected task needs it. | To do - Build first |
| R21 | The rover shall remain stable with a 5 kg test payload throughout its selected arm poses and carrying route. | Team safety target; prior IDs: MBP-002 | Test the most demanding approved arm pose and slope with a protected test setup. | To do - Build first |
| R22 | The rover and arm shall reach ground pickup poses and the selected lander controls at their expected heights within the 0-1.5 m mission envelope. | Selected scope within 2026 mission; prior IDs: ARM-015, ARM-019, ESM-001 | Use a simple full-size fixture to demonstrate the selected poses, allowing rover repositioning. | To do - Build first |
| R23 | The gripper or simple task tools shall securely grasp representative selected delivery objects and cache handles. | Selected scope within 2026 mission; prior IDs: ARM-013, ARM-017, DEL-002, DEL-005 | Test objects up to 5 kg and under 40 cm in each bounding dimension, using grasp features up to 7.5 cm diameter; include the cache handle used in R28. | To do - Build first |
| R24 | The rover shall retain its selected payload while driving the test route and during the planned link-loss response. | Team build choice; prior IDs: ARM-018 | Carry the 5 kg test payload over the route and interrupt communications. Check power-loss behavior separately under R06. | To do - Build first |

### Open choices and implementation notes

| Requirement | Open choice or note |
| --- | --- |
| R20 | Choose the loaded reach before buying actuators; reduce reach or use rover positioning where practical. |
| R22 | Choose the servicing controls and their fixture heights before fixing arm geometry; this does not promise every task at every height. |
| R23 | Choose a small representative object set, including the smallest selected grasp feature; do not size the gripper to the whole 40 cm object. |

## Delivery

| ID | Requirement | Source / basis | Verification | Status |
| --- | --- | --- | --- | --- |
| R25 | The rover shall open the selected toolbox and cache lids, retrieve an object and place it in the cache. | Selected scoring task; 2026 example; prior IDs: ARM-005, DEL-001, DEL-003 | Demonstrate the complete sequence on a simple fixture based on the released course. | To do - Build first |
| R26 | The rover shall place selected objects within the released delivery tolerance without touching the recipient or cone with the rover. | Selected scoring task; 2026 example; prior IDs: DEL-004, ARM-014 | Measure the settled object's nearest point. The 2026 course used 20 cm and allowed the object to touch the target; replace this check if 2027 changes. | To do - Build first |
| R27 | The rover and operators shall complete the chosen ground delivery sequence within the assigned mission time. | Selected scoring scope; prior IDs: DEL-010, DEL-015 | Rehearse with payload, blind C2 and route locations up to 1 km from the start; record time. General 2026 mission time was 30-60 minutes. | To do - Build first |

### Open choices and implementation notes

| Requirement | Open choice or note |
| --- | --- |
| R25 | Confirm the 2027 task and fixture before building specialized tools. |
| R27 | Choose tasks after the 2027 course is released. Do not adopt the old 35/20-minute stage plan as a 2027 rule. |

## Equipment servicing

| ID | Requirement | Source / basis | Verification | Status |
| --- | --- | --- | --- | --- |
| R28 | The rover shall pick up and transport a cache of less than 5 kg to a lander up to 100 m away. | Selected scoring task; 2026 reference; prior IDs: ESM-003 | Use a representative handle at least 10 cm long and no more than 5 cm in diameter; check that the cache stays retained. | To do - Build first |
| R29 | The rover shall release the selected lander latch and open its hinged panel. | Selected scoring task; 2026 reference; prior IDs: ESM-005 | Demonstrate on a fixture representing the released latch and panel travel. | To do - Build first |
| R30 | The arm shall operate the selected quarter-turn valve and selected buttons, switches or knobs to their requested states. | Selected scoring scope; prior IDs: ESM-011, ESM-012 | Demonstrate each selected control on a measured fixture; choose tool shape and arm precision from the test. | To do - Build first |
| R31 | The rover and operators shall complete the selected cache, panel and control sequence within 30 minutes. | Selected scoring scope; 2026 time; prior IDs: ESM-013 | Rehearse with the actual travel, approach and arm operations; record which scoring steps were completed. | To do - Build first |

### Open choices and implementation notes

| Requirement | Open choice or note |
| --- | --- |
| R30 | Choose the easiest useful control set first; other controls can be added after this set works. |

## Science

| ID | Requirement | Source / basis | Verification | Status |
| --- | --- | --- | --- | --- |
| R32 | The rover and science operators shall investigate at least two sites before selecting one returned cache, within the assigned science time. | 2026 reference plus team rehearsal target; prior IDs: SCM-001, SCM-006 | Rehearse the complete selected workflow within 20 minutes as an initial team target; 2026 allotted 20-30 minutes with sites within 0.5 km of C2. | To do - Build first |
| R33 | The rover shall record site panoramas, sampling close-ups and a nearby stratigraphic view that the team can use in its science explanation. | 2026 reference; prior IDs: SCM-002, SCM-003, SCM-004 | Check panoramas for directions and scale, close-ups for focus and scale, and the hillside view for interpretable layers; associate images with their sites. | To do - Build first |
| R34 | Site coordinates, elevation, reported accuracy, images and science results shall be saved with site identifiers and available for the debrief. | 2026 science evidence plus team recording choice; prior IDs: SCM-005, NEW-007, SOF-012, SOF-013 | Open the saved records at C2 after the practice mission and identify the site and measurement for each result. | To do - Build first |
| R35 | The rover shall perform the selected life-detection method onboard while at the site and record results that can be interpreted against appropriate controls. | 2026 reference; prior IDs: SCM-006 | Demonstrate the chosen method with known controls and explain what the result supports and cannot establish. | To do - Build first |
| R36 | The rover shall perform a second selected scientific measurement onboard at the site and record its result. | 2026 reference; prior IDs: SCM-007 | Demonstrate a known sample or reference; do not rely on returning samples to the team for laboratory analysis. | To do - Build first |
| R37 | The rover shall cache at least 5 g of material collected from below 10 cm depth, distinguished from shallower material. | 2026 reference; prior IDs: SCM-008, SCM-009 | Measure sampling depth and recovered qualifying mass in a representative soil test. | To do - Build first |
| R38 | The rover shall seal the sample onboard and return a cache that does not spill when tipped or inverted and can be removed within 5 minutes after roving ends. | 2026 reference; prior IDs: SCM-010 | Perform a tip test and timed removal; confirm judges can open it. Documented chemical treatment of cached material is permitted under 2026 rules. | To do - Build first |
| R39 | The science system shall retain all water, reagents and reaction products onboard during use and return. | 2026 reference; prior IDs: SCM-011 | Inspect the planned chemical use and check for leaks in operation and expected handling poses, following the applicable safety plan. | To do - Build first |
| R40 | Science results shall retain their site, depth and treatment history and the controls needed to interpret the chosen methods. | Team science method choice; prior IDs: NEW-005, NEW-006 | Run a blank/control and representative sample; show the record links and check carryover between samples. | To do - Build first |

### Open choices and implementation notes

| Requirement | Open choice or note |
| --- | --- |
| R35 | Select one affordable, defensible method with faculty advice before buying instruments. |
| R36 | Choose one complementary method that the team can calibrate and explain. |
| R40 | Use controls appropriate to the chosen methods; no unsupported contamination limit or laboratory quality system is proposed. |

## Autonomy

| ID | Requirement | Source / basis | Verification | Status |
| --- | --- | --- | --- | --- |
| R41 | The rover shall autonomously drive to the two precise GNSS targets and stop within 3 m of each. | Selected scope within 2026 mission; prior IDs: ANM-002, SOF-010 | Use surveyed targets and onboard arrival decisions; run without steering help from C2. | To do - Build first |
| R42 | The rover shall autonomously find a target post near the supplied GNSS point and stop within 2 m of the actual post. | Selected scope within 2026 mission; prior IDs: ANM-003, ANM-004, SOF-009 | Test both 2026 search offsets, 5-10 m and 10-20 m. Use 4x4_50 tags on 20 cm faces including borders, on three sides at 0.5-1.5 m height. | To do - First stretch |
| R43 | During autonomous travel, the rover shall avoid the obstacles in its chosen test envelope or stop when no safe route is available. | Team safety and navigation choice; prior IDs: ANM-006, SOF-011 | Place representative obstacles on the practice route and check clearance and safe stopping. | To do - Build first |
| R44 | The rover shall decide arrival onboard, stop and show an obvious arrival message at C2; a daylight-visible rear light shall show red for autonomy, blue for manual driving and flashing green for success. | 2026 reference; prior IDs: ANM-001, ANM-005 | Run a target approach and mode changes outdoors; check the light and judge display. | To do - Build first |
| R45 | The rover shall support a permitted abort return and stop within 5 m of an eligible previous location; programming shall occur only while stopped after successful arrival or a qualifying abort return. | 2026 reference and Q&A; prior IDs: ANM-009 | Test first-target return to the start and a later return. Manual return is permitted by the direct reasonable route, without scouting, for a 20% penalty on that location's available points; autonomous return has no penalty. A search coordinate qualifies for programming only during a qualifying abort return. | To do - Build first |
| R46 | The rover shall complete the chosen GNSS practice sequence within the 30-minute autonomous mission allowance. | Selected scoring scope; 2026 reference; prior IDs: ANM-010 | Rehearse navigation, stops and abort handling; the 2026 course could total up to 2 km. Add post searches only if R42 is selected; the three object-recognition objectives are deferred. | To do - Build first |

### Open choices and implementation notes

| Requirement | Open choice or note |
| --- | --- |
| R42 | Add post navigation after GNSS arrival and abort handling work reliably. It is not part of the initial build commitment. |
| R43 | Choose detectable obstacle size and clearance after the first sensor tests. Advanced boulder-field routing is deferred. |

## Field operation

| ID | Requirement | Source / basis | Verification | Status |
| --- | --- | --- | --- | --- |
| R47 | The students shall make the rover and C2 ready within 15 minutes and recover the rover and any deployables and remove all team equipment within 10 minutes. | 2026 reference; prior IDs: C2R-004, C2R-005 | Time a full setup and pack-up with the actual crew, cables, checks and tools, including recovery of a disabled rover. | To do - Build first |
| R48 | The team shall make any required battery, module and software changes and be ready for autonomy within 10 minutes after servicing. | 2026 reference; prior IDs: GEN-013 | Run the two mission sequences consecutively with the same C2; include power and mode checks. | To do - Build first |
